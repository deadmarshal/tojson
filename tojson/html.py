import json
import re
from collections import OrderedDict


from bs4 import BeautifulSoup
from nested_lookup import nested_lookup


def _gen_dict_extract(var):
    '''iterate over nested dict,
    yield tuple of each tag and its value'''
    for tag, value in var.items():
        if isinstance(value, str):
            continue
        yield (tag, value)
        if isinstance(value, dict):
            for result in _gen_dict_extract(value):
                yield result
        elif isinstance(value, list):
            for d in value:
                for result in _gen_dict_extract(d):
                    yield result


class HTML:

    def __init__(self, document, text_skip=None):
        if text_skip is None:
            text_skip = []
        self.text_skip = text_skip
        self.doc = document
        self._html_to()

    def _html_to(self):
        '''convert given HTML document to Dict'''
        self._dict = OrderedDict()
        self.soup = BeautifulSoup(self.doc, 'html.parser')
        for tag in self.soup.find_all():
            self._customize_attrs(tag)
            parent_type, tag_loc = self._get_tag_location(tag)
            try:
                for attr, value in tag.attrs.items():
                    tag_loc[attr] = value
                if tag.text and tag.name not in self.text_skip:
                    tag_loc['text'] = tag.get_text(strip=True)

            except TypeError:
                if tag.text and tag.name not in self.text_skip:
                    tag.attrs['text'] = tag.get_text(strip=True)

                if isinstance(parent_type, list):
                    tag.attrs = {tag.name: tag.attrs}
                tag_loc.append(tag.attrs)

    @staticmethod
    def _customize_attrs(tag):
        custom_attrs = {'class', 'rel'}
        for attr in custom_attrs.intersection(tag.attrs):
            x = re.search(
                r'<%s.[^<]*%s=\s*"\s*([^"]+)".*>' % (tag.name, attr), str(tag))
            tag.attrs[attr] = x.group(1)

    def _get_tag_location(self, tag):
        '''get location of tag and it's parent'''
        tag_loc = 'self._dict'
        for parent in reversed(list(tag.parents)[:-1]):
            if isinstance(eval(tag_loc), list):
                tag_loc += '[-1]'
            else:
                tag_loc += '["%s"]' % parent.name
        else:
            parent_tag_loc = tag_loc
            tag_loc += '["%s"]' % tag.name
        try:
            return None, eval(tag_loc)

        except KeyError:
            count = len(tag.parent.find_all(tag.name, recursive=False))
            exec(tag_loc + '= {}') if count == 1 else exec(tag_loc + '= []')
            return None, eval(tag_loc)

        except TypeError:
            return eval(parent_tag_loc), eval(parent_tag_loc)

    def todict(self, order=True):
        '''return dict version of HTML document
        :param order: return OrderedDict if True otherwise Dict'''
        return self._dict if order else dict(self._dict)

    def tojson(self, indent=2):
        '''return json version of HTML document
        :param: indent: json output indentation'''
        return json.dumps(self._dict, indent=indent, ensure_ascii=False)

    def __getitem__(self, tag):
        return self._dict[tag]

    def __iter__(self):
        return _gen_dict_extract(self._dict)

    def __eq__(self, other):
        if self._dict == other._dict:
            return True
        return False

    def __contains__(self, tag):
        return nested_lookup(tag, self._dict)

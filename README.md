# tojson
Python HTML document to JSON

#### convert HTML document to JSON
```
>>> from tojson import HTML
>>> with open('sample.html', 'r') as src:
...    html = HTML(src.read(), text_skip=['html', 'head', 'body'])
...    html.tojson()) # return json format of html
{
  "html": {
    "head": {
      "title": {
        "text": "test"
      }
    },
    "body": {
      "bgcolor": "FFFFFF",
      "img": {
        "src": "clouds.jpg",
        "align": "bottom"
      },
      "a": [
        {
          "href": "http://somegreatsite.com",
          "text": "Link Name"
        },
        {
          "href": "mailto:support@yourcompany.com",
          "text": "support@yourcompany.com"
        }
      ],
      "h1": {
        "text": "This is a Header"
      },
      "h2": {
        "text": "This is a Medium Header"
      },
      "p": [
        {
          "text": "first paragraph"
        },
        {
          "text": "second paragraph!"
        }
      ],
      "b": {
        "text": "This is a new sentence without a paragraph break",
        "i": {
          "text": "This is a new sentence without a paragraph break"
        }
      }
    }
  }
}
```
#### iterate over tags and their values
 to get tuple contains (tag, value):
```
>>> from tojson import HTML
>>> with open('sample.html', 'r') as src:
...    html = HTML(src.read(), text_skip=['html', 'head', 'body'])
...
>>> for item in html:
...    item
...
('html', {'head': {'title': {'text': 'test'}}, 'body': {'bgcolor': 'FFFFFF', 'img': {'src': 'clouds.jpg', 'align': 'bottom'}, 'a': [{'href': 'http://somegreatsite.com', 'text': 'Link Name'}, {'href': 'mailto:support@yourcompany.com', 'text': 'support@yourcompany.com'}], 'h1': {'text': 'This is a Header'}, 'h2': {'text': 'This is a Medium Header'}, 'p': [{'text': 'first paragraph'}, {'text': 'second paragraph!'}], 'b': {'text': 'This is a new sentence without a paragraph break', 'i': {'text': 'This is a new sentence without a paragraph break'}}}})
('head', {'title': {'text': 'test'}})
('title', {'text': 'test'})
('body', {'bgcolor': 'FFFFFF', 'img': {'src': 'clouds.jpg', 'align': 'bottom'}, 'a': [{'href': 'http://somegreatsite.com', 'text': 'Link Name'}, {'href': 'mailto:support@yourcompany.com', 'text': 'support@yourcompany.com'}], 'h1': {'text': 'This is a Header'}, 'h2': {'text': 'This is a Medium Header'}, 'p': [{'text': 'first paragraph'}, {'text': 'second paragraph!'}], 'b': {'text': 'This is a new sentence without a paragraph break', 'i': {'text': 'This is a new sentence without a paragraph break'}}})
('img', {'src': 'clouds.jpg', 'align': 'bottom'})
('a', [{'href': 'http://somegreatsite.com', 'text': 'Link Name'}, {'href': 'mailto:support@yourcompany.com', 'text': 'support@yourcompany.com'}])
('h1', {'text': 'This is a Header'})
('h2', {'text': 'This is a Medium Header'})
('p', [{'text': 'first paragraph'}, {'text': 'second paragraph!'}])
('b', {'text': 'This is a new sentence without a paragraph break', 'i': {'text': 'This is a new sentence without a paragraph break'}})
('i', {'text': 'This is a new sentence without a paragraph break'})
```

from distutils.core import setup


setup(
    name='tojson',
    version='0.1',
    description='Python Convert HTML Document to JSON',
    author='Behzad Mehrabi',
    author_email='bezMehrabi@gmail.com',
    url='https://github.com/Bezmehrabi/tojson.git',
    license='LICENSE.txt',
    install_requires=[
        'bs4 >= 0.0.1',
        'nested-lookup',
        'six'
    ]
)

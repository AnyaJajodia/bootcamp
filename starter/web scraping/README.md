# Web Scraping

Web scraping is the process of parsing a web page or website and converting part of it into structured data usually in the form of a CSV that is compatible for import into a database. Some sites restrict web scraping or limits the connections, always check the terms of use for any legal restrictions. 

## Python (Beautiful Soap)

[Beautiful Soap](https://www.crummy.com/software/BeautifulSoup/)

### Install into venv

Install Beautiful Soap 4.x
`pip install beautifulsoup4`

Install HTML/XML parsers
`pip install lxml`
`pip install html5lib`

``` python
from bs4 import BeautifulSoup

# local file path
with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# HTML source
soup = BeautifulSoup("<html>a web page</html>", 'html.parser')
```

The HTML source/doc is converted by BeautifulSoap to Unicode, and HTML entities are converted to Unicode characters in python objects, commonly used ones are;

1. Tag 
2. NavigableString
3. BeautifulSoup

### Tag

A Tag object corresponds to an XML or HTML tag

``` python
# Bold tag
soup = BeautifulSoup('<b id='title-1' class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
print(tag.name)
# All Attributes
print(tag.attrs)
# Specific attribute
print(tag['id'])
# 'title-1'
print(tag['class'])
# ['boldest']
```

You can use get_attribute_list to get a value that’s always a list, whether or not it’s a multi-valued atribute.

``` python
id_soup.p.get_attribute_list('id')
# ["title-1"]
```

### NavigableString

A `string` corresponds to a bit of text within a tag. Beautiful Soup uses the NavigableString class to contain these bits of text.

``` python
print(tag.string)
# 'Extremely bold'
print(type(tag.string))
# <class 'bs4.element.NavigableString'>
s = str(tag.string)
print(type(s))
# <type 'str'>
```

The `tag.string` is not a standard Python unicode string, it also has tree navigation and search functions that have a large memory footprint, when using the `tag.string` outside of BeautifulSoap code always convert to unicode string.

### BeautifulSoup

The BeautifulSoup object represents the parsed document. It supports most of the methods in Navigating the tree and Searching the tree.

### Tree Navigation

``` python
from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Print document
print(soup.prettify())

soup.title
# <title>The Dormouse's story</title>

soup.title.name
# u'title'

soup.title.string
# u'The Dormouse's story'

soup.title.parent.name
# u'head'

soup.p
# <p class="title"><b>The Dormouse's story</b></p>

soup.p['class']
# u'title'

soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
```

Tags may contain strings and other tags. These elements are the tag’s children. Beautiful Soup strings don’t support any of these attributes, because a string can’t have children.

The simplest way to navigate the parse tree is to say the name of the tag you want. If you want the `<head>` tag, just say `soup.head` or `soup.body.b`.

Using a tag name as an attribute will give you only the first tag by that name.

To get all the `<a>` tags, or anything more complicated than the first tag with a certain name, use `soup.find_all('a')`.

A tag’s children are available in a list called `.contents`

Instead of getting them as a list, you can iterate over a tag’s children using the `.children` generator.

``` python
head_tag = soup.head
head_tag
# <head><title>The Dormouse's story</title></head>

head_tag.contents
# [<title>The Dormouse's story</title>]

title_tag = head_tag.contents[0]
title_tag
# <title>The Dormouse's story</title>
title_tag.contents
# ['The Dormouse's story']

for child in title_tag.children:
    print(child)
# The Dormouse's story
```

The `.descendants` attribute lets you iterate over all of a tag’s children, recursively: its direct children, the children of its direct children, and so on.

``` python
for child in head_tag.descendants:
    print(child)
# <title>The Dormouse's story</title>
# The Dormouse's story
```

If a tag has only one child, and that child is a `NavigableString` its made available as `.string`

If a tag’s only child is another tag, and that tag has a `.string`, then the parent tag is considered to have the same `.string` as its child.

If a tag contains more than one thing, then it’s not clear what `.string` should refer to, so `.string` is defined to be `None`.

``` python
title_tag.string
# 'The Dormouse's story'

head_tag.contents
# [<title>The Dormouse's story</title>]
head_tag.string
# 'The Dormouse's story'

print(soup.html.string)
# None
```

If there’s more than one thing inside a tag, you can still look at just the strings. Use the `.strings` generator. These strings tend to have a lot of extra whitespace, which you can remove by using the `.stripped_strings` generator instead.

You can access an element’s parent with the `.parent` attribute.

``` python
title_tag = soup.title
title_tag
# <title>The Dormouse's story</title>
title_tag.parent
# <head><title>The Dormouse's story</title></head>

title_tag.string.parent
# <title>The Dormouse's story</title>
```

The parent of a top-level tag like `<html>` is the `BeautifulSoup` object itself. And the `.parent` of a `BeautifulSoup` object is defined as None:

``` python
html_tag = soup.html
type(html_tag.parent)
# <class 'bs4.BeautifulSoup'>

print(soup.parent)
# None
```

You can iterate over all of an element’s parents with `.parents`.

``` python
link = soup.a
link
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
for parent in link.parents:
    print(parent.name)
# p
# body
# html
# [document]
```

Direct children of the same tag are called siblings. Use `.next_sibling` and `.previous_sibling` to navigate between page elements that are on the same level of the parse tree.

``` python
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>", 'html.parser')

sibling_soup.b.next_sibling
# <c>text2</c>

sibling_soup.c.previous_sibling
# <b>text1</b>

print(sibling_soup.b.previous_sibling)
# None
print(sibling_soup.c.next_sibling)
# None
```

The strings “text1” and “text2” are not siblings, because they don’t have the same parent.

the `.next_sibling` of the first `<a>` tag is not the second `<a>` tag, but actually it’s a string: the comma and newline that separate the first `<a>` tag from the second.

You can iterate over a tag’s siblings with `.next_siblings` or `.previous_siblings`.

``` python
for sibling in soup.a.next_siblings:
    print(repr(sibling))
# ',\n'
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# ' and\n'
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# '; and they lived at the bottom of a well.'

for sibling in soup.find(id="link3").previous_siblings:
    print(repr(sibling))
# ' and\n'
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# ',\n'
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
# 'Once upon a time there were three little sisters; and their names were\n'
```

The `.next_element` attribute of a string or tag points to whatever was parsed immediately afterwards. It might be the same as `.next_sibling` but usually isn't.

``` python
last_a_tag = soup.find("a", id="link3")
last_a_tag
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

last_a_tag.next_sibling
# ';\nand they lived at the bottom of a well.'

last_a_tag.next_element
# 'Tillie'
```

The `.previous_element` attribute is the exact opposite of `.next_element`. It points to whatever element was parsed immediately before this one.

``` python
last_a_tag.previous_element
# ' and\n'
last_a_tag.previous_element.next_element
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
```

Use `.next_elements` and `.previous_element` to move forward or backward in the document as it was parsed.

### Tree Search

The two most popular methods `find()` and `find_all()`. By passing in a filter to an argument like find_all(), you can zoom in on the parts of the document you’re interested in.

- String
- Regular Expression
- List
- True
- Function: Define a `function` that takes an element as its only argument. The function should return `True` if the argument matches, and `False` otherwise.

``` python
soup.find_all('b')
# [<b>The Dormouse's story</b>]

import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
# body
# b

soup.find_all(["a", "b"])
# [<b>The Dormouse's story</b>,
#  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

for tag in soup.find_all(True):
    print(tag.name)
# html
# head
# title
# body
# p
# b
# p
# a
# a
# a
# p

def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

soup.find_all(has_class_but_no_id)
# [<p class="title"><b>The Dormouse's story</b></p>,
#  <p class="story">Once upon a time there were…bottom of a well.</p>,
#  <p class="story">...</p>]
```


`find_all(name, attrs, recursive, string, limit, **kwargs)`

The `find_all()` method looks through a tag’s descendants and retrieves all descendants that match your filters. 

``` python
soup.find_all("title")
# [<title>The Dormouse's story</title>]

soup.find_all("p", "title")
# [<p class="title"><b>The Dormouse's story</b></p>]

soup.find_all("a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find_all(id="link2")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

import re
soup.find(string=re.compile("sisters"))
# 'Once upon a time there were three little sisters; and their names were\n'

soup.find_all(id=True)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find_all(href=re.compile("elsie"), id='link1')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
```

Some attributes, like the `data-*` attributes in HTML 5, have names that can’t be used as the names of keyword arguments. Use these attributes in searches by putting them into a dictionary and passing the dictionary into `find_all()` as the `attrs` argument.

``` python
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>', 'html.parser')
data_soup.find_all(data-foo="value")
# SyntaxError: keyword can't be an expression

data_soup.find_all(attrs={"data-foo": "value"})
# [<div data-foo="value">foo!</div>]
```

You can’t use a keyword argument to search for HTML’s ‘name’ element, because Beautiful Soup uses the name argument to contain the name of the tag itself. Instead, you can give a value to ‘name’ in the `attrs` argument.

``` python
name_soup = BeautifulSoup('<input name="email"/>', 'html.parser')
name_soup.find_all(name="email")
# []
name_soup.find_all(attrs={"name": "email"})
# [<input name="email"/>]
```

Search by CSS class using the keyword argument class. As with any keyword argument, you can pass class_ a string, a regular expression, a function, or True.

``` python
soup.find_all("a", class_="sister")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find_all(class_=re.compile("itl"))
# [<p class="title"><b>The Dormouse's story</b></p>]

def has_six_characters(css_class):
    return css_class is not None and len(css_class) == 6

soup.find_all(class_=has_six_characters)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```

A single tag can have multiple values for its “class” attribute. When you search for a tag that matches a certain CSS class, you’re matching against any of its CSS classes. You can also search for the exact string value of the class attribute. But searching for variants of the string value won’t work.

To search for tags that match two or more CSS classes use a CSS selector.

``` python
css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
css_soup.find_all("p", class_="strikeout")
# [<p class="body strikeout"></p>]

css_soup.find_all("p", class_="body")
# [<p class="body strikeout"></p>]

css_soup.find_all("p", class_="body strikeout")
# [<p class="body strikeout"></p>]

css_soup.find_all("p", class_="strikeout body")
# []

css_soup.select("p.strikeout.body")
# [<p class="body strikeout"></p>]
```

Search with string argument.

``` python
soup.find_all(string="Elsie")
# ['Elsie']

soup.find_all(string=["Tillie", "Elsie", "Lacie"])
# ['Elsie', 'Lacie', 'Tillie']

soup.find_all(string=re.compile("Dormouse"))
# ["The Dormouse's story", "The Dormouse's story"]

def is_the_only_string_within_a_tag(s):
    """Return True if this string is the only child of its parent tag."""
    return (s == s.parent.string)

soup.find_all(string=is_the_only_string_within_a_tag)
# ["The Dormouse's story", "The Dormouse's story", 'Elsie', 'Lacie', 'Tillie', '...']
```

Although string is for finding strings, you can combine it with arguments that find tags. Beautiful Soup will find all tags whose .string matches your value for string.

``` python
soup.find_all("a", string="Elsie")
# [<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>]
```

Limit seatrh output with `limit` argument.

``` python
soup.find_all("a", limit=2)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
```

To limit recursion to only direct decendants/children, use argument `recursive=False`.

``` python
soup.html.find_all("title")
# [<title>The Dormouse's story</title>]

soup.html.find_all("title", recursive=False)
# []
```

Shortcut to find_all()

``` python
soup.find_all("a")
soup("a")

soup.title.find_all(string=True)
soup.title(string=True)
```

Return the first result with `find()`, saves time by not parsing rest if the document. `find_all()` returns a list containing the single result, and `find()` just returns the result. `find_all()` can’t find anything, it returns an empty list. If `find()` can’t find anything, it returns `None`:

``` python
soup.find_all('title', limit=1)
# [<title>The Dormouse's story</title>]

soup.find('title')
# <title>The Dormouse's story</title>
```

find_parents() and find_parent()
find_next_siblings() and find_next_sibling()
find_previous_siblings() and find_previous_sibling()
find_all_next() and find_next()
find_all_previous() and find_previous()

#### CSS selectors

BeautifulSoup has a .select() method which uses the `SoupSieve` package to run a CSS selector against a parsed document and return all the matching elements. Tag has a similar method which runs a CSS selector against the contents of a single tag.

``` python
soup.select("title")
# [<title>The Dormouse's story</title>]

soup.select("p:nth-of-type(3)")
# [<p class="story">...</p>]

soup.select("body a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie"  id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.select("html head title")
# [<title>The Dormouse's story</title>]

soup.select("head > title")
# [<title>The Dormouse's story</title>]

soup.select("p > a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie"  id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.select("p > a:nth-of-type(2)")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

soup.select("p > #link1")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

soup.select("body > a")
# []

soup.select("#link1 ~ .sister")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie"  id="link3">Tillie</a>]

soup.select("#link1 + .sister")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

soup.select(".sister")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.select("[class~=sister]")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.select("#link1")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

soup.select("a#link2")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

soup.select("#link1,#link2")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

soup.select('a[href]')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.select('a[href="http://example.com/elsie"]')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

soup.select('a[href^="http://example.com/"]')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.select('a[href$="tillie"]')
# [<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.select('a[href*=".com/el"]')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
```

There’s also a method called select_one(), which finds only the first tag that matches a selector,



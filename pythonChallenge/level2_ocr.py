#!/usr/bin/python

from urllib import urlopen
import re

webpage = urlopen("http://www.python.com/pc/def/ocr.html")
rawtext = webpage.read()

print rawtext

pattern = r""".*?
in the mess below
.*?
<!--
(.*?)
-->
"""
m = re.search( pattern, rawtext, re.VERBOSE )
text = m.group(1)
print text

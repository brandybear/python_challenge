__author__ = 'Brandy'

import urllib2
import string
import re

next_nothing = "8022"
for i in range(400):
    file_like_object = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + next_nothing)
    raw_string = file_like_object.read()
    print raw_string
    next_nothing = re.findall("nothing is (\d+)", raw_string)[0]

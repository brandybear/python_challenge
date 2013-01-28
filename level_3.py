__author__ = 'Brandy'

import urllib2
import string
file_like_object = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/equality.html")
raw_string = file_like_object.read()
print raw_string.find("kAewt")
cutoff = raw_string.find("kAewt")
improved_string = raw_string[cutoff:]
print improved_string
caps = [string.ascii_uppercase]
print caps

i = 0
z = len(improved_string)

for i in range(z):
    if improved_string[i].islower() and improved_string[i+1].isupper() and improved_string[i+2].isupper()and improved_string[i+3].isupper()and improved_string[i+4].islower() and improved_string[i+5].isupper() and improved_string[i+6].isupper() and improved_string[i+7].isupper()and improved_string[i+8].islower():
        print improved_string[i+1:i+8]
        if i < z:
            i = i + 1
    else:
        if i < z:
            i = i + 1

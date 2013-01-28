__author__ = 'Brandy'

import urllib2
import pickle


file_like_object = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
print pickle.load(file_like_object)

__author__ = 'Brandy'
import urllib2
import string
file_like_object = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
raw_string = file_like_object.read()
print raw_string.find("%%$@_$^")
cutoff = raw_string.find("%%$@_$^")
improved_string = raw_string[raw_string.rfind("%%$@_$^"):]
print improved_string
exclamation = []
at_symbol = []
hashtag = []
dollar = []
modulo = []
carrot = []
ampersand = []
star = []
lt_parenth = []
rt_parenth = []
underscore = []
plus = []
lt_curly = []
rt_curly = []
lt_bracket = []
rt_braclet = []
new_line = []
rare = []

for x in improved_string:
    if x == "!":
        exclamation.append("!")
    elif x == "@":
        at_symbol.append("@")
    elif x == "#":
        hashtag.append("#")
    elif x == "$":
        dollar.append("$")
    elif x == "%":
        modulo.append("%")
    elif x == "^":
        carrot.append("^")
    elif x == "&":
        ampersand.append("&")
    elif x == "*":
        star.append("*")
    elif x == "(":
        lt_parenth.append("(")
    elif x == ")":
        rt_parenth.append(")")
    elif x == "_":
        underscore.append("_")
    elif x == "+":
        plus.append("+")
    elif x == "{":
        lt_curly.append("{")
    elif x == "}":
        rt_curly.append("}")
    elif x == "[":
        lt_bracket.append("[")
    elif x == "]":
        rt_braclet.append("]")
    elif x == "\n":
        new_line.append("\n")
    else:
        rare.append(x)

print rare
print len(rare)
print len(exclamation)
print len(at_symbol)
print len(hashtag)

__author__ = 'Brandy'
import string
d = {"a":"c", "b":"d", "c":"e", "d":"f", "e":"g", "f":"h", "g":"i", "h":"j", "i":"k", "j":"l", "k":"m", "l":"n", "m":"o", "n":"p", "o":"q", "p":"r", "q":"s", "r":"t", "s":"u", "t":"v", "u":"w", "v":"x", "w":"y", "x":"z", "y":"a", "z":"b"}
phrase = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = "http://www.pythonchallenge.com/pc/def/map.html"
for x in phrase:
    if x == " ":
        print " "
    elif x == ",":
        print ","
    elif x == ".":
        print "."
    elif x == "'":
        print "'"
    elif x == "(":
        print "("
    elif x == ")":
        print ")"
    else:
        print d[x]

frm = "abcdefghijklmnopqrstuvwxyz"
to = "cdefghijklmnopqrstuvwxyzab"
translation = string.maketrans(frm, to)
print url.translate(translation)

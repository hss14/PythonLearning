#!/usr/bin/python

import string

original = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print original

dic1 = 'yz' + string.lowercase[:-2]
dic2 = string.lowercase[4:]+'abcd'

table1 = string.maketrans('mqg', 'koe')
table2 = string.maketrans( string.lowercase, dic2)
table3 = string.maketrans(dic1, string.lowercase)

print original.translate(table3)
print "map".translate(table3)

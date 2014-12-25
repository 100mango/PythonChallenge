
#challenge 0

print '%ld' % 2**32

#challenge 1
import string

translateTable = string.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')

code = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq y
pc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q 
ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
print code.translate(translateTable)

url = 'http://www.pythonchallenge.com/pc/def/map.html'
print url.translate(translateTable)



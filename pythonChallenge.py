#coding=utf-8
#challenge 0  计算

print '%ld' % 2**32

#challenge 1 字符移动，简单的解码
import string

translateTable = string.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')

code = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq y
pc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q 
ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
print code.translate(translateTable)

url = 'http://www.pythonchallenge.com/pc/def/map.html'
print url.translate(translateTable)

#challenge 2
#寻找出现频率低的符号 即需要写一个统计词频的算法
text = ''''''  #删掉了一大堆字符，需要的时候再放进来

from collections import OrderedDict
charDic = OrderedDict();

for char in text:
	if char in charDic:
		charDic[char] += 1
	else:
		charDic[char] = 1

print charDic;

#challenge3 正则匹配
#谜题URL = 'http://www.pythonchallenge.com/pc/def/equality.html'
import re

challenge3Text = ''' ''' #删掉了一大堆字符，需要的时候再放进来

match =  re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', challenge3Text)
print match





#coding=utf-8
#谜题地址：http://www.pythonchallenge.com/pc/def/linkedlist.php
import urllib
import re

response = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
html =  response.read()
#根据提示，我们需要找出下一个Nothing ,不断请求直到获得答案
nextNothing = re.findall(r'([0-9]+)', html)
print nextNothing

def goDown(nothing):
	response = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nothing)
	html = response.read();
	print html
	nextNothing = re.findall(r'([0-9]+)', html)[0]
	print nextNothing
	goDown(nextNothing)

#goDown(nextNothing[0])

#发现到了16044 会有Yes. Divide by two and keep going.因此我们把它除以2
#goDown('8022')

#然后82682：There maybe misleading numbers in the text. One example is 82683. Look only for the next nothing and the next 
#nothing is 63579

goDown('63579')
#最后得到 peak.html great!
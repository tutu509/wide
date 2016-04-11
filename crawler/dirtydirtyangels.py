#!/usr/bin/env python
#coding=utf-8
import sys
import re
import os
import requests

inFilename = sys.argv[1]
inputfile = open(inFilename,"r")
output = open("dirtydirtyangels.txt","a+")
download = open("download.txt","w+")
lines = inputfile.readline()

url = r'http://www.dirtydirtyangels.com/ajax.php?s=user_login'
user = {'username':'peashooter','password':'lk1906045247'}
s = requests.Session()
r = s.post(url,data = user)
while lines:

	html = s.get(lines)
	webpattern = re.compile(r'cnf.*?\'(http.*?)\'')
	webmatch = webpattern.search(html.text)
	#print webmatch.group(1)
	src = webmatch.group(1)
	srcpage = s.get(src)
	urlpattern = re.compile(r'(http://media.*?)]')
	urlmatch = urlpattern.search(srcpage.text)
	titlepattern = re.compile(r'title[\s\S]*?\[.*?\[(.*?)]]>')
	titlematch = titlepattern.search(srcpage.text)
	print urlmatch.group(1),titlematch.group(1)
	download.write("%s\n" % urlmatch.group(1))
	output.write("%s |%s\n" % (urlmatch.group(1),titlematch.group(1)))
	lines = inputfile.readline()
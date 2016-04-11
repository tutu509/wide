#!/usr/bin/env python
#coding=utf-8
import sys
import re
import os
import requests

reload(sys)
sys.setdefaultencoding('utf8')

inFilename = sys.argv[1]
inputfile = open(inFilename,"r")
output = open("out.txt","a+")
download = open("download.txt","w+")

lines = inputfile.readline()
while lines:
	web = requests.get(lines)
	mainpattern = re.compile(r'(http.*?)/show')
	webpattern = re.compile(r'(/play-.*?)"')
	mainmatch = mainpattern.search(lines)
	webmatch = webpattern.search(web.text)
	print webmatch.group(1)
	weburl = requests.get(mainmatch.group(1)+webmatch.group(1))
	#print weburl.text
	videopattern = re.compile(r'file: \'(.*?)\'[\s\S]*title: \'(.*?)\'')
	videomatch = videopattern.search(weburl.text)
	print videomatch.group(1),videomatch.group(2)

	output.write("%s |%s\n" % (videomatch.group(1),videomatch.group(2)))
	download.write("%s\n" % videomatch.group(1))
	lines = inputfile.readline()

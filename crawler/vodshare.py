#!/usr/bin/env python
#coding=utf-8
import sys
import re
import os
import requests

reload(sys)
sys.setdefaultencoding('utf8')

output = open("out.txt","a+")

inFilename1 = sys.argv[1]
web = requests.get(inFilename1)
webpattern = re.compile(r'(/play-.*?)"')
webmatch = webpattern.search(web.text)
#print webmatch.group(1)
weburl = requests.get('http://sex880.com'+webmatch.group(1))
#print weburl.text
videopattern = re.compile(r'file: \'(.*?)\'[\s\S]*title: \'(.*?)\'')
videomatch = videopattern.search(weburl.text)
print videomatch.group(1),videomatch.group(2)

output.write("%s %s" % (videomatch.group(1),videomatch.group(2)))

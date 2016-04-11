#!/usr/bin/env python
#coding=utf-8
import sys
import re
import os

reload(sys)
sys.setdefaultencoding('utf8')

inFilename = sys.argv[1] #example out.xt or dirtydirtyangels.txt
oldpattern = re.compile(r'(http.*?) ')
newpattern = re.compile(r'\|(.*)\n')
inRead = open(inFilename, "r")
lines = inRead.readline()
while lines:
	oldmatch = oldpattern.search(lines)
	newmatch = newpattern.search(lines)
	oldname = os.path.basename(oldmatch.group(1))
	newname = newmatch.group(1)
	print oldname,newname
	if os.path.isfile(oldname):
		os.rename(oldname,newname.decode("utf-8").encode("GBK")+".mp4")
	lines = inRead.readline()


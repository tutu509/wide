#!/usr/bin/env python
import sys
import re
import os
inFilename = sys.argv[1]
if os.path.isfile(inFilename):
    namelength = inFilename.rfind(".")
    name = inFilename[0:namelength]
    exten = inFilename[namelength:]
    outFilename = name + "_in_new" + exten

print "inFilename:", inFilename
print "outFilename:", outFilename


fpRead = open(inFilename, "r")
fpWrite = open(outFilename, "w+")

EndPattern = re.compile(r'end')

s = '0'

tag = 1
while bool(tag):
    linePattern1 = re.compile(r'(%s)\s.*\s([0-9]+)'% s)#把变量s作为匹配pattern
    tag = 0
    i = 0
    fpRead.seek(0)
    lines = fpRead.readline()
    while lines:

        match1 = linePattern1.search(lines)
        endmatch = EndPattern.search(lines)
        if match1:

            i = int(match1.group(2))+i
            tag = 1 

        lines = fpRead.readline()
    fpWrite.write("%s  %d\n" %(s,i))
    s = str(int(s)+1)
fpRead.close()
fpWrite.close()

#!/usr/bin/env python
import sys
import re
import os
inFilename1 = sys.argv[1]
inFilename2 = sys.argv[2]
if os.path.isfile(inFilename1):
    namelength = inFilename1.rfind(".")
    name = inFilename1[0:namelength]
    exten = inFilename1[namelength:]
    outFilename1 = name + "_total" + exten

if os.path.isfile(inFilename2):
    namelength = inFilename2.rfind(".")
    name = inFilename2[0:namelength]
    exten = inFilename2[namelength:]
    outFilename2 = name + "_total" + exten


print "inFilename:", inFilename1,inFilename2
print "outFilename:", outFilename1,outFilename2


inRead = open(inFilename1, "r")
outRead = open(inFilename2, "r")
inWrite = open(outFilename1, "w+")
outWrite = open(outFilename2, "w+")


s = '0'

tag = 1
while bool(tag):
    linePattern1 = re.compile(r'(%s)\s.*\s([0-9]+)'% s)
    tag = 0
    i = 0
    inRead.seek(0)
    lines = inRead.readline()
    while lines:

        match1 = linePattern1.search(lines)
        if match1:

            i = int(match1.group(2))+i
            tag = 1 

        lines = inRead.readline()
    inWrite.write("%s  %d\n" %(s,i))
    s = str(int(s)+1)

s = '0'

tag = 1
while bool(tag):
    linePattern1 = re.compile(r'(%s)\s.*\s([0-9]+)'% s)
    tag = 0
    i = 0
    outRead.seek(0)
    lines = outRead.readline()
    while lines:

        match1 = linePattern1.search(lines)
        if match1:

            i = int(match1.group(2))+i
            tag = 1 

        lines = outRead.readline()
    outWrite.write("%s  %d\n" %(s,i))
    s = str(int(s)+1)
inRead.close()
outRead.close()
inWrite.close()
outWrite.close()

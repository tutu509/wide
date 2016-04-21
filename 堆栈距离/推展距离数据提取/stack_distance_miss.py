#!/usr/bin/env python
import sys
import re
import os
inFilename = sys.argv[1]
pidFile = sys.argv[2]
strpattern = sys.argv[3]
if os.path.isfile(inFilename):
	namelength = inFilename.rfind(".")
	name = inFilename[0:namelength]
	exten = inFilename[namelength:]
	outFilename1 = name+"-inorder"+exten
	outFilename2 = name+"-outorder"+exten

print "inFilename:", inFilename,pidFile
print "outFilename:", outFilename1,outFilename2

pidRead = open(pidFile,"r")
fpRead = open(inFilename, "r")
#inWrite = open(outFilename1,"w+")
#outWrite = open(outFilename2,"w+")


i = 0
j = 0
n = 0
misses_all = 0.0
accesses_all = 0.0
sample_num = 0.0

missPattern = re.compile(r'dcache.Out_Of_Order_Stack_Distance_Distribution::0.1(\s.*?)([0-9|\.]+)')
accessPattern = re.compile(r'dcache.Out_Of_Order_Stack_Distance_Distribution::(\d+)\s.*?([0-9|\.]+)')
samplePattern = re.compile(r'dcache.Out_Of_Order_Stack_Distance_Distribution::samples(\s.*?)([0-9|\.]+)')
threadbeginPattern = re.compile(r'Begin Simulation Statistics')
threadendPattern = re.compile(r'End Simulation Statistics')
pidPattern = re.compile(r'%s' % strpattern)
pidlines = pidRead.readline()
while pidlines:
    tag = False
    i = i+1
    pidmatch = pidPattern.search(pidlines)
    if pidmatch:
	num = i
	fplines = fpRead.readline()
	while fplines:
            beginmatch = threadbeginPattern.search(fplines)
            if beginmatch:
                j = j+1
            if num == j:
                tag = True
                while fplines:
                    missmatch = missPattern.search(fplines)
                    accessmatch = accessPattern.search(fplines)
                    samplematch = samplePattern.search(fplines)
                    endmatch = threadendPattern.search(fplines)
                    if missmatch:
                        print missmatch.group(2),missmatch.group()
                        n = n+1
                        misses_all = float(missmatch.group(2))+misses_all
                    if accessmatch:
                        if (int(accessmatch.group(1))>1):
                            accesses_all = float(accessmatch.group(2))+accesses_all
                       	    print accessmatch.group(2),accessmatch.group()
                    if samplematch:
                        sample_num = float(samplematch.group(2))+sample_num
                    if endmatch:
                        break
                    fplines = fpRead.readline()
            if tag:
                break
            fplines = fpRead.readline()
    pidlines = pidRead.readline()
rate = (misses_all+accesses_all)/sample_num
print rate,n

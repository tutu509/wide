#!/usr/bin/env python
import sys
import re
import os
inFilename = sys.argv[1]
if os.path.isfile(inFilename):
	namelength = inFilename.rfind(".")
	name = inFilename[0:namelength]
	exten = inFilename[namelength:]
	outFilename = name+"-collect-special_back"+exten

print "inFilename:", inFilename
print "outFilename:", outFilename

fpRead = open(inFilename, "r")
fpWrite = open(outFilename, "w+")

switchdtbPattern = re.compile(r'(Stack_Distance_Distribution_In_Order::)(\d.*?\s).* (\s[0-9|\.]+)')
stackoutPattern = re.compile(r'(dcache.Out_Of_Stack_Distance_Distribution::)(\d.*?\s).*(\s[0-9|\.]+)')
threadbeginPattern = re.compile(r'Begin Simulation Statistics')
threadendPattern = re.compile(r'End Simulation Statistics')
lines = fpRead.readline()
def stack(a,last):
    intval = int(a)
    diff = intval-last
    i = 1
    while (diff > i):
        print last+i,0
        fpWrite.write("%d   0\n" % (last+i))
        i = i+1
    last = intval
    return last


while lines:
#	linesmatch = linesPatter.match(lines)
	threadbeginmatch = threadbeginPattern.search(lines)
#	threadendmatch = threadendPattern.match(lines)
        #lineswrite = linesmatch.group(1)
        # print "----------------------- reading lines------------------"
	if threadbeginmatch:
                last1 = 0
                last2 = 0
                print "------------------------ entering thread -------------------"
		threadlines = fpRead.readline()
#                threadendmatch = threadendPattern.match(threadlines)
		while threadlines:
#           print threadlines
			stackinmatch = switchdtbPattern.search(threadlines)
                        stackoutmatch = stackoutPattern.search(threadlines)
                        threadendmatch = threadendPattern.search(threadlines)
                        if stackinmatch:
                            last1 = stack(stackinmatch.group(2),last1)
                            '''
                            intval = int(stackinmatch.group(2))
                            diff = intval-last1
                            i = 1
                            while (diff > i):
                                print "%d   0"% (last1+i)
                                fpWrite.write("%d   0\n" % (last1+i))
                                i = i+1
                            last1 = intval
                            '''
                            print stackinmatch.group(2),stackinmatch.group(3)
                            fpWrite.write("%s %s\n" %(stackinmatch.group(2),stackinmatch.group(3)))
                        if stackoutmatch:
                            '''
                            intval = int(stackoutmatch.group(2))
                            diff = intval-last2
                            i = 1
                            while (diff > i):
                                print "%d   0"% (last2+i)
                                fpWrite.write("%d   0\n" % (last2+i))
                                i = i+1
                            last2 = intval
                            '''
                            print stackoutmatch.group(2),stackoutmatch.group(3)
                            fpWrite.write("%s %s\n" %(stackoutmatch.group(2),stackoutmatch.group(3)))
			if threadendmatch:
			#	fpWrite.write("\n")
                            print "------------------------ thread collection done!! --------------------"
                            fpWrite.write("------------------------------------------------------\n")
                            break
                        threadlines = fpRead.readline()
        lines = fpRead.readline()
fpRead.close()
fpWrite.close()


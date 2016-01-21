#!/usr/bin/env python
import sys
import re
import os
inFilename = sys.argv[1]
pidFile = sys.argv[2] #another input file
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
inWrite = open(outFilename1,"w+")
outWrite = open(outFilename2,"w+")

def stack(a,last,n):  #add those stack distributions whose numbers is 0
    intval = int(a)
    diff = intval-last
    i = 1
    while (diff > i):
        print last+i,0
        if n == 1:
        	inWrite.write("%d   0\n" % (last+i))
        else:
        	outWrite.write("%d   0\n" % (last+i))
        i = i+1
    last = intval
    return last

i = 0 #pidfile's line number
j = 0 #statsfile's thread number

switchdtbPattern = re.compile(r'(Stack_Distance_Distribution_In_Order::)(\d.*?\s).* (\s[0-9|\.]+)')
stackoutPattern = re.compile(r'(dcache.Out_Of_Order_Stack_Distance_Distribution::)(\d.*?\s).*(\s[0-9|\.]+)')
threadbeginPattern = re.compile(r'Begin Simulation Statistics')
threadendPattern = re.compile(r'End Simulation Statistics')
pidPattern = re.compile(r'qsort_large') #pattern for target thread
pidlines = pidRead.readline()
while pidlines:
	tag = False #flag to stop searching statsfile
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
				tag = True #enable flag
				last1 = 0 #record the last stack distribution number for in-order
                last2 = 0
				while fplines:
					stackinmatch = switchdtbPattern.search(fplines)
					stackoutmatch = stackoutPattern.search(fplines)
					endmatch = threadendPattern.search(fplines)
					if stackinmatch:
						last1 = stack(stackinmatch.group(2),last1,1)
						print stackinmatch.group(2),stackinmatch.group(3)
						inWrite.write("%s %s\n" %(stackinmatch.group(2),stackinmatch.group(3)))
					if stackoutmatch:
						last2 = stack(stackoutmatch.group(2),last2,2)
						print stackoutmatch.group(2),stackoutmatch.group(3)
                        outWrite.write("%s %s\n" %(stackoutmatch.group(2),stackoutmatch.group(3)))
                    if endmatch:
                    	inWrite.write("------------------------------------------------------\n")
                    	outWrite.write("------------------------------------------------------\n")
                    	break #thread end,break out of the loop
                    fplines = fpRead.readline() #next line
            if tag:
            	break #stop searching thread number
            fplines = fpRead.readline()
    pidlines = pidRead.readline()
pidRead.close()
fpRead.close()
inWrite.close()
outWrite.close()
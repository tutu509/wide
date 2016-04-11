#coding=utf-8
import os

path=os.getcwd()
files=os.listdir(path)
a='1'
for item in files:
	if item[item.find('.'):]!='.py':
		os.rename(item,a+'.jpg')
		a=str(int(a)+1)
		print a
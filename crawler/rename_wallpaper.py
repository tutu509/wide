#coding=utf-8
import os

path=os.getcwd()
files=os.listdir(path)
a='1'
for item in files:
	if item[item.find('.'):]!='.py':
		while os.path.exists(a+'.jpg'):
			a=str(int(a)+1)
		os.rename(item,a+'.jpg')
		print a
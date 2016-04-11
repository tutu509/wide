#coding=utf-8
import urllib2
import urllib
import cookielib
import sys
import time
import re
#data={"accont":"system","password":"**********"}  #登陆用户名和密码
#post_data=urllib.urlencode(data)
def remaintime():
	count=17
	while (count>0):
		count-=1
		time.sleep(1)
		print "%d \r" % (count),
		pass
	pass

post_data='account=%E5%B0%8F%E5%9B%BE&password=lk825145247&remember=0&url_back=http%3A%2F%2Fwww.zimuzu.tv%2F'
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
headers ={"User-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"}
req=urllib2.Request("http://www.zimuzu.tv/User/Login/ajaxLogin",post_data,headers)
print u"登录中···".encode("GBK")
content=opener.open(req)
headers_refer ={"User-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36","Connection":"keep-alive","refer":"http://www.zimuzu.tv/user/sign"}
print u"转入签到页面···".encode("GBK")
checkreq=urllib2.Request("http://www.zimuzu.tv/user/sign",None,headers)
check=opener.open(checkreq)
#time.sleep(17)
remaintime()
print u"签到···".encode("GBK")
signreq=urllib2.Request("http://www.zimuzu.tv/user/sign/dosign",None,headers)#其实不用伪装
sign=opener.open(signreq)
#z=sys.getdefaultencoding()
#print check.read().decode("utf-8").encode("GBK")
check=opener.open(checkreq)

match=re.search("(font class=\"f2\">)(\d*?)<",check.read())
print match.group(2)
fwrite=open("days.txt","a+")
fwrite.write("%s   " % match.group(2))
fwrite.close()
time.sleep(15)
#!/bin/usr/python
#import webbrowser, sys, pyperclip 
import urllib2
response=urllib2.urlopen ('http://pythonforbeginners.com/') # ('http://urlscan.io/')
print (response.info())

#sample content below, note: python2 being used
#Date: Wed, 23 Jan 2019 06:16:08 GMT
#Content-Type: text/html; charset=utf-8
#Transfer-Encoding: chunked
#Connection: close
#Server: Apache/2.4.33 (Amazon) mod_wsgi/3.5 Python/2.7.14
html = response.read()
response.close()


#!/usr/bin/python 
import urllib, sys, time
#import urllib.parse  

#def urldecode(url):
#	return urllib.parse.unquote(url)
url = input("Enter the data to be encoded: ")
time.sleep(1)
urllib.unquote(url).decode('utf8')
print("Here is your output")
print urllib.unquote(url).decode('utf8')
#for line in sys.stdin:
#   sys.stdout.write(urllib.unquote(line))	 decoding uri 


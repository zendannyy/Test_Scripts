#!/usr/bin/python
# for python 2.7 only
import base64, binascii, struct, string
code = raw_input("Enter the data you wish to be decoded from Base64: ")
answer=code.decode('base64','strict')
print ("Here is your output")
print (answer)

'''if input = base64 :
	base64.decode '''
'''def base64_decode(input,errors='strict') : 
	assert errors == 'strict'
	output = base64.decodestring(input)
	return (output, len(input)) # from base_64_codec  '''


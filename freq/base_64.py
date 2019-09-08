#!/usr/bin/python
code = raw_input("Enter the data you wish to be encoded to Base64: ")
answer=code.encode('base64','strict')
print ("Here is your output") 
print (answer)

def base64_decode(input,errors='strict') : # this procudes no results, errors, etc. 
    	#assert errors == 'strict'
        #output = base64.decodestring(input)
	if input is 'base64':
	        return (output, len(input)) 
	else:
		print ("No output")

'''
from base64 import b64decode
import binascii
def base64(string, base):
    string = b64decode(string)
    string = ensure_str(string)
    if string in decoded:
        Quit()
    print(g + ' Decoded from Base64 : %s' % (string))
    decoded.append(string)
    decode(string, 'none')
    decode(base, 'b64')
    Quit()
'''
# https://github.com/s0md3v/Decodify/blob/master/dcode

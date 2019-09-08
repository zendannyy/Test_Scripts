#!/usr/bin/python2.7  
''' Example
codecs.decode(codecs.decode('0a', 'hex'),'ascii')
u'\n'
or
codecs.decode("707974686f6e2d666f72756d2e696f", "hex").decode('utf-8')
u'python-forum.io'
'''
'''Example: for more brevity 
codecs.decode("0a", "hex").decode('ascii')
u'\n'
'''
'''
import hex, binascii, struct, string
import codecs 
answer = raw_input("Enter the data you wish to be decoded from hex: ")
#binascii.a2b_hex(codecs.replace('', '')).decode('hex') #codecs.decode('hex', 'hex').decode('ascii')
print ("Here is your output")
print (answer)
'''
import codecs, binascii
#decode_hex = codecs.getdecoder("hex_codec")

answer = raw_input("Enter the data you wish to be decoded from hex: ")

# binascii.a2b_hex(codecs.replace('', '')).decode('hex')
print ("Here is your output")
print (answer)
binascii.unhexlify(''.join(''.split()))

#!/usr/bin/python
code = raw_input("Enter the data you wish to be encoded to Base64")
answer=code.encode('rot13','strict') # based off caesar cipher
print (answer)

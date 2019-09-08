#!/usr/bin/python
import sys, math
def byte(decimal) :
	return int(math.log(decimal, 2)) + 1
def main() :
	# Asks user for a decimal number
	decimal = input("Type an integer: ")
	dec = decimal
	#Converts decimal to Hex
	hexa = hex(dec)
	#Converts decimal to binary
	binary = "{0:b}".format(dec)
	print("Decimal: ", dec)
	print("Hexadecimal: ", hexa)
	print("Binary", binary)
	a = byte(dec) # This links the dec variable, to the byte function which states how big the input is in Bits
	print("Size of number typed: ", a, " Bits")	# displays the converted values of the decimal you typed
main()

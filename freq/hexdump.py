#!/usr/bin/python
def hanndler(packet):
	hexdump(packet.payload)
sniff(count=20, prn=handler)


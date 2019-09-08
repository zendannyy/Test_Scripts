#!/usr/bin/python

# Parses a Malwarebytes Breach Remediation for Mac log file and outputs a json file
# with information on what was removed and when.
# Works on any system that is supported by Breach Remediation for Mac.

# To use, run as follows:
#   python parse_log.py -i /path/to/mbbr/log.txt -o /path/to/output/log.json

# The sample code described herein is provided on an "as is" basis,
# without warranty of any kind, to the fullest extent permitted by
# law.Malwarebytes does not warrant or guarantee the individual success
# developers may have in implementing the sample code on their development
# platforms. You are solely responsible for testing and maintaining all
# scripts.

# Malwarebytes does not warrant, guarantee or make any representations
# regarding the use, results of use, accuracy, timeliness or completeness
# of any data or information relating to the sample code. Malwarebytes
# disclaims all warranties, express or implied, and in particular,
# disclaims all warranties of merchantability, fitness for a particular
# purpose, and warranties related to the code, or any service or software


import re
import json
import socket
import sys, getopt

inputFile = ''
outputFile = ''

try:
	opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
except getopt.GetoptError:
	print 'usage: parse_log.py -i <inputFile> -o <outputFile>'
	sys.exit(2)
for opt, arg in opts:
	if opt == '-h':
		print 'usage: parse_log.py -i <inputFile> -o <outputFile>'
		sys.exit()
	elif opt == '-i':
		inputFile = arg
	elif opt == '-o':
		outputFile = arg

if inputFile == '' or outputFile == '':
# debugging:
#	inputFile = 'log.txt'
#	outputFile = 'log.json'
	print 'usage: parse_log.py -i <inputFile> -o <outputFile>'
	sys.exit()
	
removal_events = []
startPattern = re.compile(r"""(\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2}:\d{2}) : Removing detected threats\.\.\.""", re.IGNORECASE)
removalEventPattern = re.compile(r"""\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2}:\d{2} : +[^ ]* Removing [a-z ]*item:\s+(.+)$""", re.IGNORECASE)
endPattern = re.compile(r"""\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2}:\d{2} : [- ]*Threat removal complete[- \.]*""", re.IGNORECASE)

parsingEvents = False
removedFileCount = 0
with open(inputFile) as f:
	for line in f:
		if parsingEvents:
			match = endPattern.match(line)
			if match:
				# End this event
				removal_event["removed_file_count"] = removed_file_count
				removal_event["removed_files"] = removed_files
				removal_events.append(removal_event)
				parsingEvents = False
				continue
			match = removalEventPattern.match(line)
			if match:
				# Add this item to the log
				fileRemoved = match.group(1)
				removed_files.append(fileRemoved)
				removed_file_count = removed_file_count + 1
		else:
			match = startPattern.match(line)
			if match:
				# Start building a removal event
				parsingEvents = True
				removal_event = {"removal_start_time" : match.group(1)}
				removed_files = []
				removed_file_count = 0

logData = {}

logData["hostname"] = socket.gethostname()
logData["ip_address"] = socket.gethostbyname(socket.getfqdn())
logData["removal_events"] = removal_events

with open(outputFile, "w") as f:
	json.dump(logData, f, indent=2)

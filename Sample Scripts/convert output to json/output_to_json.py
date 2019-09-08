#!/usr/bin/python

# version 1.1

# Runs a scan with Malwarebytes Breach Remediation, as specified by the
# scanCommand variable. The output is then parsed and output to stdout in
# JSON format.

# Note that this script must be run with root permissions, as all scans
# require root.

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
# purpose, and warranties related to the code, or any service orsoftware
# related there to.


import subprocess
import re
import json

scanCommand = 'mbbr scan -remove -noreboot'

proc=subprocess.Popen( scanCommand, shell=True, stdout=subprocess.PIPE, )
output=proc.communicate()[0]
#output='Scanning with signatures version 167 (2017-2-12)\rMalwarebytes Breach Remediation 1.2.6.730\rCopyright (c) 2016 Malwarebytes.  All rights reserved.\rScanning... \rAdware.FkCodec : /Users/treed/Library/LaunchAgents/com.codecm.uploader.plist\rOSX.Genieo : /Users/treed/Library/Application Support/Google/Chrome/Default/Extensions/GoldenBoy_test_ch\rOSX.Genieo : /Applications/Genieo.app\rFiles detected: 3\r*** Scan time: 0d 00:00:16 ***\rScan complete.\rThreats were not removed.'

detections = []
processingDetections = False
postDetections = False
for oneLine in output.splitlines():
	if processingDetections:
		if oneLine.startswith('Files detected:') or ('did not find any threats' in oneLine):
			break
		detections.append(oneLine)
		
	else:
		if oneLine.startswith('Scanning...'):
			processingDetections = True

threatsFound = len(detections)
detectionDict = {'threatsFound' : threatsFound}
if 'Some of the threats require a reboot' in output:
	detectionDict['needsReboot'] = 'true'
else:
	detectionDict['needsReboot'] = 'false'
	
detectionList = []
if detections:
	for oneDetection in detections:
		parts = oneDetection.split(' : ')
		threatName = parts[0]
		threatType = threatName.split('.')[0]
		if threatType == 'OSX' or threatType == 'Trojan':
			threatType = 'Malware'
		threatPath = parts[1]
		detectionList.append({'threatName' : threatName, 'threatType' : threatType, 'threatPath' : threatPath})

detectionDict['detectedThreats'] = detectionList
detectionJSON = json.dumps(detectionDict, indent=2)

print detectionJSON
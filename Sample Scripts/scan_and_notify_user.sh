#!/bin/bash

# IMPORTANT! This script MUST be run with root privileges. Most remote admin
# platforms will allow you to run scripts as root. If you are running the script
# directly, run it with sudo, like so:

# sudo /path/to/script/scan_and_notify.sh

# Runs a scan using Malwarebytes Breach Remediation for Mac, removes threats found,
# then parses the output and sends a notification to the user about the results.

# This script assumes the mbbr executable is in /usr/local/bin. If it is not,
# change the MBBRPATH variable to the proper path to the folder containing
# the mbbr executable.

# Note that Breach Remediation for Mac logs are not pruned at this point, and
# this script does not attempt to parse only data from the latest scan, so it
# will output information about everything that has been detected for the
# life of the current log file.

# https://www.malwarebytes.org/business/breachremediation/

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

MBBRPATH='/usr/local/bin'

cd $MBBRPATH

REG="$(./mbbr register)"
UPD="$(./mbbr update)"
OUTPUT="$(./mbbr scan -remove -noreboot)"

THREATSFOUND=$(printf '%s' "$OUTPUT" | sed -nE 's/Files detected: ([0-9]+)/\1/p')
printf '%s' "$OUTPUT" | grep -q 'Some of the threats require a reboot'
if [ $? -eq 0 ] ; then
	NEEDSREBOOT=1
else
	NEEDSREBOOT=0
fi
MALWARECOUNT=$(printf '%s' "$OUTPUT" | egrep -ic '[-0-9 :]*(OSX|Trojan)\.')
if [ -z $MALWARECOUNT ] ; then
	MALWARECOUNT="0"
fi
NL=$'\n'

if [ ! -z $THREATSFOUND ] ; then
	MSG="Found $THREATSFOUND threat files. $MALWARECOUNT of the threats were malware."
	if [ $NEEDSREBOOT -gt 0 ] ; then
		MSG="$MSG${NL}A reboot is required to finish the removal process."
	fi
	
	osascript -e "display notification \"$MSG\" with title \"Threats were removed\""
fi
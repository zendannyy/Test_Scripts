#!/bin/bash

# IMPORTANT! This script MUST be run with root privileges. Most remote admin
# platforms will allow to do so. If you are running the script
# directly, run it with sudo, like so:

# sudo /path/to/script/scan_and_parse.sh

# Runs a scan using Malwarebytes Breach Remediation for Mac, then
# parses the resulting log file and takes action based on whether malware,
# adware or PUPs were found. The action in this sample is to echo an alert
# about what was found along with the paths to the detected files.

# This script assumes the mbbr executable is in /usr/local/bin. If it is not,
# change the MBBRPATH variable to the proper filepath containing the mbbr executable.

# Note that Breach Remediation for Mac logs are not pruned at this point, and
# this script does not attempt to parse only data from the latest scan, so it
# will output information about everything that has been detected for the
# life of the current log file.

# https://www.malwarebytes.org/business/breachremediation/

# The sample code described herein is provided on an "as is" basis,
# without warranty of any kind, to the fullest extent permitted by
# law.Malwarebytes does not warrant or guarantee the individual success
# developers may have in implementing the sample code on their development
# platforms. You are solely responsible for testing and maintaining all scripts.


MBBRPATH='/usr/local/bin'

cd $MBBRPATH

MACHINEID=$(./mbbr register | sed -nE 's/Machine ID:[[:space:]]*([0-9A-Z]*)/\1/p')
./mbbr update
./mbbr scan

INFILE="${MBBRPATH}/mbbr-logs/${MACHINEID}log.txt"

egrep -iq '[-0-9 :]*(OSX|Trojan)\.' $INFILE
if [ $? -eq 0 ] ; then
	# Malware was detected!!! Sound the red alert!
	echo -e '\nMalware was found!!!\n'
	sed -nE 's/[-0-9 :]*(OSX|Trojan)\.[^:]* : (.*)/\2/p' <$INFILE
else
	# No malware found, whew!
	echo -e '\nNo malware found\n'
fi

egrep -iq '[-0-9 :]*Adware\.' $INFILE
if [ $? -eq 0 ] ; then
	# Adware was found
	echo -e '\nAdware was found\n'
	sed -nE 's/[-0-9 :]*Adware\.[^:]* : (.*)/\1/p' <$INFILE
else
	# No adware found
	echo -e '\nNo adware found\n'
fi

egrep -iq '[-0-9 :]*PUP\.' $INFILE
if [ $? -eq 0 ] ; then
	# PUPs were found
	echo -e '\nPUPs were found\n'
	sed -nE 's/[-0-9 :]*PUP\.[^:]* : (.*)/\1/p' <$INFILE
else
	# No PUPs found
	echo -e '\nNo PUPs found\n'
fi

echo -e '\n'

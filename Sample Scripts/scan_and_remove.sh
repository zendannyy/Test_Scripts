#!/bin/bash

# IMPORTANT! This script MUST be run with root privileges. Most remote admin
# platforms will allow you to run scripts as root. If you are running the script
# directly, run it with sudo, like so:

# sudo /path/to/script/simple_scan.sh

# Runs a scan and removal using Malwarebytes Breach Remediation for Mac,
# and echoes messages that identify whether threats were removed or not and
# whether a reboot is required.

# This script assumes the mbbr executable is in /usr/local/bin. If it is not,
# change the MBBRPATH variable to the proper path to the folder containing
# the mbbr executable.

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

REGRESULTS=$(./mbbr register)
UPDRESULTS=$(./mbbr update)
SCANRESULTS=$(./mbbr scan -remove -noreboot)
echo "$SCANRESULTS" | grep -q 'Some of the threats require a reboot'
if [ $? -eq 0 ]
then
	echo "Threats were removed, and a reboot is required."
else
	echo "$SCANRESULTS" | egrep -q 'Files detected:\s*[0-9]+'
	if [ $? -eq 0 ]
	then
		echo "Threats were removed, but did not require a reboot."
	else
		echo "No threats were removed."
	fi
fi
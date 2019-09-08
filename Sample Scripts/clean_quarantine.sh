#!/bin/bash

# IMPORTANT! This script MUST be run with root privileges. Most remote admin
# platforms will allow you to run scripts as root. If you are running the script
# directly, run it with sudo, like so:

# sudo /path/to/script/clean_quarantine.sh

# Can be run at any point to permanently delete files from the Breach
# Remediation quarantine folder.

# This script assumes that the quarantine folder is set to the default. If you
# have changed it, be sure to change the QUARPATH variable to the proper
# full path to the quarantine folder.

# Note that this script will use the infamously-dangerous rm -rf command,
# but makes every attempt to do so safely. However, you will need to be sure
# to provide a meaningful and correct value for QUARPATH.

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

QUARPATH='/Library/Application Support/com.malwarebytes.quarantine'

if [[ -z $QUARPATH ]] || [[ $QUARPATH = '/' ]]
then
	echo "Invalid quarantine path, please use another."
	exit 1
fi

echo -e "Are you sure you want to delete the entire contents of the folder:\n   $QUARPATH"
read -p "? (Y/N) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
	# Okay, you asked for it!
	rm -rf "${QUARPATH}"/*
else
	echo "Deletion cancelled."
fi
#!/bin/bash

# Echoes the installed version of Malwarebytes Breach Remediation for Mac
# to stdout. If Breach Remediation is not installed, echoes 0.

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

if [ ! -f mbbr ]
then
	echo "0"
else
	VERSION=$(./mbbr version | sed -nE 's/Program ver:[[:space:]]*([0-9\.]*)/\1/p')
	echo $VERSION
fi
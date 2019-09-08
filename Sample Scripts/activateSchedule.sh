#!/bin/sh
# Copyright (c) 2010, JAMF Software, LLC
#
####################################################################################################
#
# SUPPORT FOR THIS PROGRAM
#
# 	This program is distributed "as is" by JAMF Software, LLC's Resource Kit team. For more 
#	information or support for the Resource Kit, please utilize the following resources:
#
#		http://list.jamfsoftware.com/mailman/listinfo/resourcekit or http://www.jamfsoftware.com/support/resource-kit
#
####################################################################################################
#
# NAME
#	activateSchedule.sh - Activates the scheduled updates on target computer(s); name of the schedule must be included in the command.
# SYNOPSIS
#	sudo activateSchedule.sh
#	sudo actiavteSchedule.sh <targetVolume> <computerName> <username> <dfUsername> <dfPassword> <scheduleName>
#
# DESCRIPTION
#
#	Ativates a schedule that is currently configured in the DeepFreeze application.
#	Please note that the schedule object must already be present on the computers on which this script is ran. 
#	If the schedule is not currently available on the target clients, it can be packaged up and deployed via Composer(For packages & config files.)
#
####################################################################################################
#
# HISTORY
#
#	Version: 1.0
#
# DEFINE VARIABLES & READ IN PARAMETERS
#
####################################################################################################

# HARDCODED VALUES SET HERE
dfUsername=""
dfPassword=""
scheduleName="" # Example "Macintosh HD"


# CHECK TO SEE IF A VALUE WAS PASSED IN PARAMETER 4 AND, IF SO, ASSIGN TO "DFUSERNAME"
if [ "$4" != "" ] && [ "$dfUsername" == "" ];then
    dfUsername=$4
fi

# CHECK TO SEE IF A VALUE WAS PASSED IN PARAMETER 5 AND, IF SO, ASSIGN TO "DFPASSWORD"
if [ "$5" != "" ] && [ "$dfPassword" == "" ];then
    dfPassword=$5
fi

# CHECK TO SEE IF A VALUE WAS PASSED IN PARAMETER 6 AND, IF SO, ASSIGN TO "SCHEDULENAME"
if [ "$6" != "" ] && [ "$scheduleName" == "" ];then
    scheduleName=$6
fi
# 
# SCRIPT CONTENTS - DO NOT MODIFY BELOW THIS LINE
#
####################################################################################################

if [ "$dfUsername" == "" ];then
	echo "Error:  The parameter 'dfUsername' is blank.  Please specify a user."
	exit 1
fi

if [ "$dfPassword" == "" ];then
	echo "Error:  The parameter 'dfPassword' is blank.  Please specify a password."
	exit 1
fi

if [ "$scheduleName" == "" ];then
	echo "Error:  The parameter 'scheduleName' is blank.  Please specify the name of the DeepFreeze schedule you would like to activate."
	exit 1
fi

/Library/Application\ Support/Faronics/Deep\ Freeze/CLI "$dfUsername" "$dfPassword" activateSchedule "$scheduleName"

exit 0	# Graceful exit code 
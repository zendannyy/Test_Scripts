#!/bin/bash

# takes input as an epoch timestamp
# returns a human readable timestamp in ISO format 

# Check if an argument was provided
if [ -z "$1" ]; then
    echo "Usage: $0 <epoch_timestamp>"
    exit 1
fi


# Store the epoch timestamp as a variable
epoch_timestamp="$1"
os=$(uname)

# macOS
if [ "${os}" = "Darwin" ]; then
    # Use the 'date' command to convert the epoch timestamp to ISO format
    iso_date=$(date -u -r "${epoch_timestamp}" +"%Y-%m-%dT%H:%M:%SZ")
elif [ "{$os}" = "Linux" ]; then
    # For Linux use this 
    iso_date=$(date -u -d "${epoch_timestamp}" +"%Y-%m-%dT%H:%M:%SZ")
else
    echo "Appear to be running an Unsupported OS: "${os}" "
    exit 1
fi 

# Print the resulting ISO date
echo "ISO Date: ${iso_date}"


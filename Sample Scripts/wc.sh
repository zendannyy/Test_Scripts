#!/bin/bash
for F in *.csv ; do 
wc -l "$F" 

#grep -c "/usr/local/jenkinsd.sh" "$F"
done 
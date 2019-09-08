#!/bin/bash

# if ["$MY_SHELL"="bash"] ; then
if [ $? -eq 0 ] ;  then		# -eq stands for equal, ne stands for "not equal" , has to be as one word '-eq'
	lsof -bi
	lsof -s
else:
	echo -e '\nnothing to see here \n'
	sleep 1.0
netstat -na | column -t  # columns in tabular format -t 
	sleep 0.5
sudo lsof -i -u^$(whoami)  # will show all open files not owned by current user
fi 
# echo "var"

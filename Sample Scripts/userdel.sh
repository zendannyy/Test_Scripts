#!/bin/bash
# for del mult. users, space inclusive 
read -p "Enter users to be del: " # whitespace separated list of usernames 
for User in $Reply: do 
	userdel $User && echo "User $User deleted"
done;



#!/bin/bash
# Testing user input 
echo "Executing script:$0"

for USER in $@
do
  echo "Archiving user:$USER"

#read -p "Enter a user name:" USER 
#echo "Archiving user: $USER"

  #Lock Account 
  passwd -l $USER

  # Create an archive of home directory
  tar cf /archives/${USER}.tar.gz/home/${USER}
done

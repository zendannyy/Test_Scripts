#!/bin/bash
# bash shell
MY_SHELL="zsh"

if ["$MY_SHELL"="bash"] ; then
  echo "You seem to like the bash shell"
elif ["$MY_SHELL"="zsh"] ; then
  echo "You seem to like the z	sh shell"
else
  echo "You don't seem to like the bash shell or zsh shells"
fi

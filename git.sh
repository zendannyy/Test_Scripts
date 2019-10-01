#!/bin/bash
#from local dir
# chmod +x
git init
git fetch
git add -A
git commit -m "updating"

git pull
git push -u origin master
# push(){
# git remote add origin repo URL
# git remote -v

#!/bin/bash
# from local dir
chmod +x
git init
git add -A
git commit -m "updating"

# git remote add origin repo URL
# git remote -v
git pull
git push origin master
git push -u origin master

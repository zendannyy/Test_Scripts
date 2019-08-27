#!/bin/bash
# from local dir
# push(){
	chmod +x
	git init
	git fetch
	git add -A
	git commit -m "updating"

	# git remote add origin repo URL
	# git remote -v
	git pull
	git push -u origin master

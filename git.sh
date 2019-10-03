#!/bin/bash
#from local dir
# chmod +x
#git init
#git fetch
#git add -A
#git commit -m "updating"

function current_branch() {
	git_current_branch
}

git init
git fetch
git add -A
git commit -m "updating"

git pull $current_branch
git push $current_branch	# -u origin master
# git remote add origin repo URL
# git remote -v

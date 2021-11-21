#!/usr/bin/env bash
# chmod +x

# How to use this script
function display_usage() {
  echo -e "Run script like this: \n./git.sh < within a git project dir>"
}

if [[ ( "${@}" == "--help") ||  "${@}" == "-h" ]]; then 
	display_usage
	exit 0
fi

function current_branch() {
	git_current_branch
}

git init
git fetch
git add -A; git commit -m "updating files"

git pull $current_branch
git push $current_branch
# git remote add origin repo URL
# git remote -v

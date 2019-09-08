#!/bin/bash
#from local dir
# chmod +x
git init
git fetch
git add -A
git commit -m "updating"

git pull
git push -u origin master
=======
# from local dir
# push(){
<<<<<<< HEAD
	chmod +x
	git init
	git fetch
	git add -A
	git commit -m "update"

	# git remote add origin repo URL
	# git remote -v
	git pull
	git push -u origin master
=======

	# git remote add origin repo URL
	# git remote -v
# >>>>>>> 5a7d288a021ce49ec102feb1f6d17e785e1aab3e
>>>>>>> ca8231129a49210bbdaf49047eb3f40c453e9a71

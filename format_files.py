#!/usr/bin/python3
"""grabbing a list of files, converting timestamps from epoch to human-readable
for files like this
1442530823_1442530758_916_7FBA7677-38AE-4DF6-AC81-409A68A72AC9.txt"""

import argparse
import time
import os
import sys


def convert_time_to_human_readable(stmp):
	"""convert timestamps to human readable
	"""
	converted_value = time.strftime("%m-%d-%Y_%H-%M-%S", time.localtime(stmp))
	return converted_value

def ls_equivalent(directory):
	"""last mod time for files in dir
	@rtype: object
	"""
	dir_files = os.scandir(directory)
	for file in dir_files:
		if file.is_file():
			ls_stat = os.stat(file)
			print("Last modified time for {} is {}".format(file.name, convert_time_to_human_readable(ls_stat.st_mtime)))


def ls_file(file):
	"""last mod time for file given at the cli"""
	# if file.is_file():
	ls_stat = os.stat(file)
	print("Last modified time for {} is {}".format(file, convert_time_to_human_readable(ls_stat.st_mtime)))

def rename(old_name, new_name):
	"""using os.rename to rename file"""
	os.rename(old_name, new_name)


def convert_epoch_to_human_readable(input_epoch):
	"""takes epoch value and converts to human readable
	time.strftime("%m-%d-%Y_%H-%M-%S", time.localtime(1442530758))
	'09-17-2015_15-59-18'
	"""
	converted_epoch_value = time.strftime("%m-%d-%Y_%H-%M-%S", time.localtime(input_epoch))
	return converted_epoch_value

def main():
	parser: ArgumentParser = argparse.ArgumentParser(
		description="""Supply the directory you want to format files for. Will print human readable timestamped files.
			Option to rename files. 
			usage: format_files.py [-h] [-d DIRECTORY] [-r RENAME]""")
	parser.add_argument('-d', '--directory', required=False, help='Formats files within the directory')
	parser.add_argument('-f', '--file', required=False, help='Formats the file given')
	parser.add_argument('-r', '--rename', nargs='+', required=False, help='Renames the files with new format')
	args = parser.parse_args()
	print(args.rename, "converted")

	if len(sys.argv) < 2:
		sys.exit(parser.description)

	# if args.directory:
	# 	ls_equivalent(args.directory)
	if args.file:
		ls_file(args.file)

	if args.rename:
		rename(old_name=args.rename[0],
			   new_name="{}.txt".format(convert_epoch_to_human_readable(args.file)))


if __name__ == '__main__':
	main()

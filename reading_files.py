#!/usr/bin/env python3
"""read files to then get their timestamps and convert them"""
from datetime import datetime
import time
import gzip

TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

def convert_times(stmp):
	"""converting timestamps to human readable"""
	timestamp = datetime.utcfromtimestamp(int(stmp))
	# timestamp = datetime.utcfromtimestamp(int(stmp[0]))
	return timestamp

def get_files():
	"""retrieve filenames from single file"""
	# output = []
	with open('/Users/dzendejas/Splunk_Backups/pinterest-spokane-cpe-paths.txt', 'r') as f:
		for line in f:
			output = line.strip().split('_')
			# underscore = line.split('_')

		# start = convert_times(output[0]).strftime(TIME_FORMAT)
 		# end = convert_times(output[1]).strftime(TIME_FORMAT)
		start = convert_times(output[0]).strftime(TIME_FORMAT)
		end = convert_times(output[1]).strftime(TIME_FORMAT)
		print("Fetching {}".format(convert_times(output[1]).strftime(TIME_FORMAT))) # to avoid timestamp = datetime.utcfromtimestamp(int(stmp[0]))
		print("{} - {}".format(start, end))


if __name__ == '__main__':
	get_files()

# TODO: account for output[0]
# 0 is not the first timestamp in 1524773859_1510170737_423_3BADDA81-473D-4172-9D28-848B3EF65D42/# when printing output list, it reads all files correctly, just can't access them by index properly

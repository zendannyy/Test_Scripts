#!/usr/bin/python3
'''following script uses requests to make GET requests w/ vt's API
https://developers.virustotal.com/reference#file-report'''
import os
import sys
import requests

if len(sys.argv) < 2:
    print("Usage: Run script as follows: vs.py hash ")
    sys.exit()

hash = ' '.join(sys.argv[1:])

class VTSafe:
	'''docstring for VTSafe class, holding the key and parameters'''
	def __init__(self):
		'''To retrieve the key'''
		super(VTSafe, self).__init__()
		self.apikey = os.environ.get("APIKEY")
		self.params = {'apikey': self.apikey, 'resource': hash}

	def get_request(self):
		'''Get request for hash that is specified by user as input'''
		# use 4107de199cda7dec5015bc92e0e48c35 when needing to test for a hash of <= 10
		# use f3774e816bd8562fcb1e1ef3f12e5e70 when testting for a hash of >= 10
		response = requests.get("https://www.virustotal.com/vtapi/v2/file/report", self.params)
		r = response.json()
		
		try:
			if r['positives'] >= 10:	# greater than 10 hits
				print("malicious threshold met, investigate")
				print(r['permalink'])
		except KeyError as ke:
			print("Not found in virustotal:", hash)


		try:
			if r['positives'] <= 10:
				print("malicious confidence & threshold not met for"), print(r['md5'])
		except KeyError as e:
			print("Not found in virustotal:", hash)
		finally:
			pass

if __name__ == '__main__':
	vt = VTSafe()
	vt.get_request()

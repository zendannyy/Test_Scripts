#!/usr/bin/env python3
"""following script uses requests to make GET requests w/ VT's API
https://developers.virustotal.com/reference#file-report
The idea is you have a specific IOC to lookup in VT, and want a quick response at the CLI """
import os
import sys
import argparse
import requests


class VTSafe:
	"""for VTSafe class, holding the key and parameters"""
	def __init__(self):
		"""To retrieve the key"""
		super(VTSafe, self).__init__()
		self.apikey = os.environ.get("APIKEY")

	def domain_lookup(self, domain):
		"""Get request for domain specified at the CLI"""
		params = {'apikey': self.apikey, 'resource': domain}
		response = requests.get("https://www.virustotal.com/vtapi/v2/domain/report", params)
		d = response.json()

		try:
			if d['positives'] >= 3:
				print("malicious threshold met, investigate")
				print(d['permalink'])
			elif d['positives'] <= 3:
				print("malicious threshold not met for:" + str(resource))
		except KeyError as ke:
			print("Not found in virustotal:", domain)

	def hash_lookup(self, hash):
		"""Get request for hash that specified by user as input"""
		# use 4107de199cda7dec5015bc92e0e48c35 when needing to test for a hash of <= 10
		# use f3774e816bd8562fcb1e1ef3f12e5e70 when testing for a hash of >= 10
		params = {'apikey': self.apikey, 'resource': hash}
		response = requests.get("https://www.virustotal.com/vtapi/v2/file/report", params)
		h = response.json()

		try:
			if h['positives'] >= 5:		# greater than 10 hits
				print("malicious threshold met, investigate")
				print(h['permalink'])
			elif h['positives'] <= 5:
				print("malicious confidence & threshold not met for: " + str(h['md5']))
				print(str(h['positives']) + " hits")

		except KeyError as ke:
			print("Not found in virustotal:", hash)
		finally:
			pass

	def url_lookup(self, url):
		"""Get request for URL specified at the CLI"""
		params = {'apikey': self.apikey, 'resource': url}
		response = requests.get("https://www.virustotal.com/vtapi/v2/url/report", params)
		u = response.json()

		try:
			if u['positives'] >= 3:
				print("malicious threshold met, investigate")
				print(u['permalink'])
			elif u['positives'] <= 3:
				print("malicious threshold not met for:" + str(resource))
		except KeyError as ke:
			print("Not found in virustotal:", url)


def main():
	"""main instantiates VTSafe class and executes functionality for all functions"""
	vt = VTSafe()

	parser = argparse.ArgumentParser(description="""CLI tool for VT's API. You can make requests for a domain, URL, 
										or hash.""")
	parser.add_argument('-d', '--domain', help='Performs a domain lookup for the domain entered')
	parser.add_argument('-hash', help='Performs a hash lookup for the hash entered')
	parser.add_argument('-u', '--url', help='Performs a URL lookup for the URL')
	parser.add_argument('--domain-file', help='Performs domain lookups for domains listed in the input file')
	parser.add_argument('--hash-file', help='Performs hash lookups for hashes listed in the input file')
	parser.add_argument('--url-file', help='Performs URL lookups for URLs listed in the input file')

	args = parser.parse_args()

	if len(sys.argv) < 2:
		sys.exit("Usage: Run script as follows: vs.py -hash hash\n\n"
				 	"vs.py -h for full help details")

	if args.domain:
		resource = args.domain
		vt.domain_lookup(args.domain)

	if args.domain_file:
		vt.process_file(args.domain_file, 'domain')

	if args.hash:
		resource = args.hash
		vt.hash_lookup(args.hash)

	if args.hash_file:
		vt.process_file(args.hash_file, 'hash')

	if args.url:
		# resource = args.url
		vt.url_lookup(args.url)
	
	if args.url_file:
		vt.process_file(args.url_file, 'url')


if __name__ == '__main__':
	main()

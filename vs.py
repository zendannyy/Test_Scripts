#usr/bin/python
# following script uses requests module to make GET requests w/ vt's API  seems to only work on python3 
import requests			
import datetime
params = {'apikey': '', 'resource': 'hashes_file'}		# Changed order of params here 
response = requests.get('https://www.virustotal.com/api/v2/file/report', params)
r = response.json()
print(r['positives'])	# using dictionaries to call keys 
# for hash in hashes_file:
	if r['response'] >= 10:	# greater than 10 hits , using dictionaries to call key:value 
		print ("malicious threshold met, investigate") , print(r['md5'])
	else:
		print ("malicious confidence & threshold not met for") , print(r['md5'])
		formatted_text = r.json()
		# print (json.response())		# if full json output is prefererred 

#  url = 'https://www.virustotal.com/vtapi'/v2/file/scan' 	#for file scan

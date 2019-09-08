#usr/bin/python
# following script uses requests module to make GET requests w/ vt's API  seems to only work on python3 
import requests			
params = {'apikey': , 'resource': hashes_file}		# Changed order of params here 
response = requests.get('https://www.virustotal.com/api/v2/file/report', params)
r = response.json()
for hash in hashes_file:
	if (r['response'] >= 10:	# greater than 20 hits 	# using dictionaries to call key:value 
		print ("malicious threshold met, investigate")
	else:
		print ("malicious confidence & threshold not met")
		print (json.response())

#  url = 'https://www.virustotal.com/vtapi'/v2/file/scan' 	#for file scan

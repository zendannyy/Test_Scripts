#!/usr/bin/python3
'''following script uses requests to make GET requests w/ vt's API'''
import os
import sys
import requests

if len(sys.argv) < 2:
    print("Usage: Run script as follows: vs.py hash ")
    sys.exit()

hash = ' '.join(sys.argv[1:])

class VTSafe:
    '''docstring for VTSafe class'''
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
        print(r['positives'])
        # print(response.json())

        if r['positives'] >= 10:	# greater than 10 hits, using dict to call value
            print("malicious threshold met, investigate")
            print(r['permalink'])
        else:
            print("malicious confidence & threshold not met for"), print(r['md5'])

if __name__ == '__main__':
    vt = VTSafe()
    vt.get_request()

# url = 'https://www.virustotal.com/vtapi'/v2/file/scan' 	#for file scan

# Combine vs.py and vt_safe
# Done

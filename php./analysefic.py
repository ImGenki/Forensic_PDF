import requests
import sys
import time

url = "https://www.virustotal.com/api/v3/files"

files = {"file": (sys.argv[1], open(sys.argv[1], "rb"), "application/pdf")}
headers = {
    "accept": "application/json",
    "x-apikey": "03b1f11837623cc37e7a1cf590df86bbcbbe5fb836fcb32a7aa2580acf2c244b"
}

response = requests.post(url, files=files, headers=headers)
temp=response.json()
print(temp['data']['id'])

url2 = "https://www.virustotal.com/api/v3/analyses/"+temp['data']['id']

headers = {
    "accept": "application/json",
    "x-apikey": "03b1f11837623cc37e7a1cf590df86bbcbbe5fb836fcb32a7aa2580acf2c244b"
}
c=0
response = requests.get(url2, headers=headers)
while(c!=1):
	if(response.json()['data']['attributes']['status']=='queued'):
		time.sleep(30)
		response = requests.get(url2, headers=headers)
	else:
		c=1
		print(response.text)
"""
Code by: Amirtha Krishnan octohands@gmail.com
Version: 0.1
Descripton: Zoho clip pomodoro extension.
Requirements: requests,json,sys
"""

import requests,json,sys,time,ctypes

def wtimer(work):
    start = work.time()
    work.clock()
    elapsed = 0
    while elapsed < work:
        elapsed = work.time() - start
    btimer(break);
    response.put("text","Break time!");
    
def btimer(break):
    start = break.time()
    break.clock()
    elapsed = 0
    while elapsed < break:
        elapsed = break.time() - start
    btimer(work);
    response.put("text","Time to get back to work!");

token="1001.c40a3fd8d0ea86a10cb6e84fcf8713ea.6993f035f6b48e4677c2b32fdf73008a"
sentby="poppyProductivity"
destination=sys.argv[1]
subject=sys.argv[2]
message=sys.argv[3]

urldest="https://cliq.zoho.com/api/v2/channelsbyname/" + (destination) + "/message"

headers = {
        "Content-type": "application/json",
        "Authorization": "Zoho-authtoken " + (token)
        }

content = {
		"text": (message),
		"broadcast" :"true",
		"bot": {
			"name": (sentby)
			},
		"card": {
			"title": (subject),
			"theme": "modern-inline"
			}
		}


post = requests.post(url=urldest, data=json.dumps(content), headers=headers)

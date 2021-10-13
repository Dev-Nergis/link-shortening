import config
import json
import requests
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

linkRequest = {
  "destination" : input('주소 : ')
  , "domain": { "fullName": "s-u.kro.kr" }
  , "slashtag": input('슬래시태그 : ')
  , "title": input('타이틀 : ')
}

requestHeaders = {
  "Content-type": "application/json",
  "apikey": "556e1816bddb4d6883c6c6b4b9d94832"
}

r = requests.post("https://api.rebrandly.com/v1/links", 
    data = json.dumps(linkRequest),
    headers=requestHeaders)

if (r.status_code == requests.codes.ok):
    link = r.json()
    print("긴주소 : %s, 짧은주소 : https://%s" % (link["destination"], link["shortUrl"]))

print("Enter to close")
while 'x' != input() :Enter

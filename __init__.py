import urllib.request
import urllib.parse
import json


with open('resume_base64.bin', 'r') as myfile:
    base64_Resume=myfile.read().replace('\n', '')



resume_json = {
        'first_name': 'Cory',
        'last_name' : 'Bond',
        'email' : '[YOUR_EMAIL_HERE',
        'position_id' : 'STE',
        'explanation' : 'Simple python script I made today. Uses urllib to make a post request to the url endpoint with my data formatted as a json object. I used the website: http://www.motobit.com/util/base64-decoder-encoder.asp to encode my pdf into a file with my base64. The json is encoded in utf-8.',
        'project' : ['https://github.com/CoryBond/CBTEN'],
        'source' : 'I found [COMPANY_NAME_HERE] first on AngelList. I did more research about your company on your own website and it looks like a fantastic place to grow a career!',
        'resume' : base64_Resume
    }
#urllib.urlopen("http://abc.com/api/posts/create",urllib.urlencode(resume_json))

#print(base64_Resume)

req = urllib.request.Request('[JSON_RECIEVER_URL]')
req.add_header('Content-Type', 'application/json')

#data = urllib.parse.quote_plus(json.dumps(resume_json))
with urllib.request.urlopen(req,json.dumps(resume_json).encode('utf-8')) as f:
    resp = f.read()
    print(resp)

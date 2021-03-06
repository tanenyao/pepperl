import urllib.request
import json

user = "admin"
pw = "private"

top_level_url = 'http://192.168.1.188'

ref_one = 25
ref_two = 255.0

p = urllib.request.HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, top_level_url, user, pw)

auth_handler = urllib.request.HTTPDigestAuthHandler(p)
opener = urllib.request.build_opener(auth_handler)

open = urllib.request.install_opener(opener)

input_num = 3

def distance(input):
	a = input[0] * ref_one
	b = input[1] / ref_two * ref_one
	b = round(b,2)
	c = a + b
	return c

try:
	forceon = urllib.request.Request('http://192.168.1.188/w/force.lr?cmd=fm&po=0&ch=0&v=1')	# v: 0-OFF 1-ON
	result = opener.open(forceon)

	for i in range(input_num):
		x = urllib.request.Request('http://192.168.1.188/w/force.lr?cmd=pm&po='+str(i)+'&ch=0&v=4')		# v: 0-Inactive 1-DigitalInput 2-DigitalOutput 3-IO-LinkSIO 4-IO-Link
		result = opener.open(x)

	while True:
		x1_data = urllib.request.Request('http://192.168.1.188/r/ioldetails.lr?port=0&_')
		result = opener.open(x1_data)
		x1_data = result.read()
		x1_data = json.loads(x1_data.decode("utf-8"))
		x1_raw = x1_data["iol"]["data"]["input"]
		print('x1: ' + str(distance(x1_raw)))

		x2_data = urllib.request.Request('http://192.168.1.188/r/ioldetails.lr?port=1&_')
		result = opener.open(x2_data)
		x2_data = result.read()
		x2_data = json.loads(x2_data.decode("utf-8"))
		x2_raw = x2_data["iol"]["data"]["input"]
		print('x2: ' + str(distance(x2_raw)))

		x3_data = urllib.request.Request('http://192.168.1.188/r/ioldetails.lr?port=2&_')
		result = opener.open(x3_data)
		x3_data = result.read()
		x3_data = json.loads(x3_data.decode("utf-8"))
		x3_raw = x3_data["iol"]["data"]["input"]
		print('x3: ' + str(x3_raw)+'\n')

		# (mapping function here)

except IOError as e:
	print(e)

# SERVER EXPECTS: POST /
# Data: [{"path": "some-path", "message": "some-message"}]
try:
	import simplejson as json
except:
	import json

import urllib2
HOST = "localhost"
PORT = 8004

class CorneliusError: pass

def update(path, message):
	updates(((path, message), ))

def updates(updates):
	global HOST, PORT
	
	# Collect updates
	data = []
	for update in updates:
		path, message = update
		data.append({ "path": path, "message": message })
		
	# Produce JSON
	value = json.dumps(data)
	
	# Request
	req = urllib2.Request("http://" + HOST + ":" + str(PORT) + "/", value)
	result = urllib2.urlopen(req)
	
	# Check result
	res = result.read()
	if res == "{success:true}":
		return True
	else:
		raise CorneliusError()

def connect(uid, paths):
	res = []
	for p in paths:
		res.append( ("::connect", uid + "->" + path) )
	return updates(res)

def disconnect(uid, paths):
	res = []
	for p in paths:
		res.append( ("::disconnect", uid + "->" + path) )
	return updates(res)

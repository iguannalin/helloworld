#
# Main app APIs
#
from flask import Flask, request
import helper as Helper
import store as Store
import os

store = {}
nodePort = 8080 if not os.getenv('PORT') else os.getenv('PORT')
nodeIP = '0.0.0.0' if not os.getenv('IP') else os.getenv('IP')
nodeID = nodeIP[-1:]
host = nodeIP

app = Flask(__name__)
#
# General
#
@app.route('/hello/')
def hello():
	return 'Hello world!'

@app.route('/whoami/')
def getID():
	return  'This is ' + nodeID

@app.route('/echo/')
def simpleGet():
	if not request.args.get('msg'):
		return ''
	return request.args.get('msg')

#
# Store
#
@app.route('/kv-store/<key>', methods=['GET'])
def storeGet(key):
	response, st = "", 200
	if key not in store:
		response, st = "{'result':'Error','msg':'Key does not exist'}", 404
	else:
		response = "{'result':'Success','value':'"+str(store[key]+"'}")
	return Helper.createResponse(response, st)

@app.route('/kv-store/<key>', methods=['DELETE'])
def storeDelete(key):
	response, st = "", 200
	if key not in store:
		response, st = "{'result':'Error','msg':'Key does not exist'}", 404
	else:
		del store[key]
		response = "{'result':'Success'}"
	return Helper.createResponse(response, st)

@app.route('/kv-store/<key>', methods=['PUT', 'POST'])
def storePut(key):
	if nodeID != '0':
		return redirect('http://'+host+':8083')

	response, st = "", 200
	val = request.form.to_dict()['val'] if 'val' in request.form.to_dict() else None
	
	if not val:
		response = "{'result':'Error','msg':'No value provided'}"
	elif Helper.isInvalid(key,val) or not request.form:
		response = "{'result':'Error','msg':'Key not valid'}"
	elif key not in store:
		response, st = "{'replaced':'False', 'msg':'New key created'}", 201
		store[key] = val
	else:
		response, st = "{'replaced':'True', 'msg':'Value of existing key replaced'}", 201
		store[key] = val
	return Helper.createResponse(response,st)

if __name__ == '__main__':
	app.run(host=nodeIP, port=nodePort, debug=True)
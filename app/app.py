#
# Main app APIs
#
from flask import Flask, request
import helper as Helper
import os

app = Flask(__name__)
store = {}
nodeIP = os.getenv('IP')
nodeID = os.getenv('IP')[-1:]
host = 'localhost'
#
# General
#
@app.route('/hello/')
def hello():
	return 'Hello world! This is ' + nodeID

@app.route('/echo/')
def getWithMsg():
	if not request.args.get('msg'):
		return ''
	return request.args.get('msg')

#
# Store
#
@app.route('/kv-store/<key>', methods=['GET'])
def storeGet(key):
	if nodeID != '0':
		return redirect('http://'+host+':8083/hello')

	response, st = "", 200
	if key not in store:
		response, st = "{'result':'Error','msg':'Key does not exist'}", 404
	else:
		response = "{'result':'Success','value':'"+str(store[key]+"'}")
	return Helper.createResponse(response, st)

@app.route('/kv-store/<key>', methods=['DELETE'])
def storeDelete(key):
	if nodeID != '0':
		return redirect('http://'+host+':8083')

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
	app.run(port=8080, debug=True)
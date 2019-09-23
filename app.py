#
# Main app APIs
#
from flask import Flask, jsonify, request, Response
import helper as Helper

app = Flask(__name__)
store = {}

#
# General
#
@app.route('/hello/')
def hello():
	return 'Hello world!'

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
	if key not in store:
		return Response("{'result':'Error','msg':'Key does not exist'}", status=404)
	else:
		return Response(f"{{'result':'Success','value':{store[key]}}}")

@app.route('/kv-store/<key>', methods=['DELETE'])
def storeDelete(key):
	if key not in store:
		return Response("{'result':'Error','msg':'Key does not exist'}", status=404)
	else:
		del store[key]
		return Response("{'result':'Success'}")

@app.route('/kv-store/<key>', methods=['PUT', 'POST'])
def storePut(key):
	val = request.form.to_dict()['val'] if 'val' in request.form.to_dict() else None
	
	if not request.form or Helper.isInvalid(key,val):
		return jsonify({'result':'Error','msg':'Key not valid'})

	response, st = {'replaced':'False', 'msg':''}, 200
	if key not in store:
		response['msg'] = 'New key created'
	else:
		st = 201
		response['replaced'] = 'True'
		response['msg'] = 'Value of existing key replaced'

	store[key] = val
	return Response(str(response),status=st)


if __name__ == '__main__':
	app.run(port=8080, debug=True)
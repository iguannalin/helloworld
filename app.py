from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello/')
def hello():
	return 'Hello world!'

@app.route('/echo/')
def getWithMsg():
	if not request.args.get('msg'):
		return ''
	return request.args.get('msg')

app.run(port=8080, debug=True)
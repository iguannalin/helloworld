from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
	return jsonify('Hello world!')

@app.route('/echo/<key>')
def get(key):
	return jsonify(key)

app.run(port=8080, debug=True)
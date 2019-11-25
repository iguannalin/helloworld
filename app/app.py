#
# Main app APIs
#
from flask import Flask, request
import helper as Helper
# import store as Store
import os

store = { }
node_port = 8080 if not os.getenv('PORT') else os.getenv('PORT')
node_ip = '0.0.0.0' if not os.getenv('IP') else os.getenv('IP')
node_id = node_ip[-1:]
host = node_ip

app = Flask(__name__)


#
# General
#
@app.route('/hello/')
def hello():
  return 'Hello world!'


@app.route('/whoami/')
def get_id():
  return 'This is ' + node_id


@app.route('/echo/')
def simple_get():
  if not request.args.get('msg'):
    return ''
  return request.args.get('msg')


#
# Store
#
@app.route('/kv-store/<key>', methods=['GET'])
def store_get(key):
  response, st = "", 200
  if key not in store:
    response, st = "{'result':'Error','msg':'Key does not exist'}", 404
  else:
    response = "{'result':'Success','value':'" + str(store[key] + "'}")
    return Helper.create_response(response, st)


@app.route('/kv-store/<key>', methods=['DELETE'])
def store_delete(key):
  response, st = "", 200
  if key not in store:
    response, st = "{'result':'Error','msg':'Key does not exist'}", 404
  else:
    del store[key]
    response = "{'result':'Success'}"
  return Helper.create_response(response, st)


@app.route('/kv-store/<key>', methods=['PUT', 'POST'])
def store_put(key):
  # if node_id != '0':
  #     return redirect('http://' + host + ':8083')

  response, st = "", 200
  val = request.form.to_dict()['val'] if 'val' in request.form.to_dict() else None

  if not val:
    response = "{'result':'Error','msg':'No value provided'}"
  elif Helper.is_invalid(key, val) or not request.form:
    response = "{'result':'Error','msg':'Key not valid'}"
  elif key not in store:
    response, st = "{'replaced':'False', 'msg':'New key created'}", 201
    store[key] = val
  else:
    response, st = "{'replaced':'True', 'msg':'Value of existing key replaced'}", 201
    store[key] = val
    return Helper.create_response(response, st)


if __name__ == '__main__':
  app.run(host=node_ip, port=node_port, debug=True)

#!flask/bin/python
from flask import Flask, jsonify, request
import sys

# change this in your own code; a litle hacky, I know.
sys.path.insert(0,'')
from challenge import scholarship_selection

app    = Flask(__name__)
arrays = []

@app.route('/scholarship_api')
def index():
	return "scholarship arrays: {}".format(arrays)

@app.route('/scholarship_api/<int:array_id>',methods=['GET'])
def answer(array_id):
	if not arrays:
		return jsonify({'sequence': None, 'total': None})

	array  = [arr for arr in arrays if arr['id'] == array_id]
	answer = scholarship_selection.scholarship_selection(array[0]['array'])

	return jsonify(answer)

@app.route('/scholarship_api', methods=['POST'])
def post_array():
	
	array = {
	'id': arrays[-1]['id'] + 1 if arrays else 0,
	'array': request.json['array'],
	}
	arrays.append(array)
	return jsonify(array), 201

if __name__ == '__main__':
    app.run(debug=True)
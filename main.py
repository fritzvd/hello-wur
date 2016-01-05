import os
from flask import Flask
from flask import request

from haversine import haversine

app = Flask(__name__)

@app.route('/')
def hello():
	template = 'Hello {}'
	name = request.args.get('name', 'World')
	return template.format(name)

@app.route('/distance')
def distance():
	from_string = request.args.get('from', None)
	to_string = request.args.get('to', None)

	if from_string is not None and to_string is not None:
		print([float(i) for i in from_string.split(',')])
		from_location = [float(item) for item in from_string.split(',')]
		to_location = [float(item) for item in to_string.split(',')]
		return '{}'.format(haversine(from_location, to_location))
	else:
		return 'Try again by using URL parameters \'from\' and \'to\' like so: distance?from=53.3,4.4&to=51.4,3.6'

if __name__ == '__main__':
	app.run(debug=True)

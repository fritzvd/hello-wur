import os
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
	template = 'Hello {}'
	name = request.args.get('name', 'World')
	return template.format(name)

if __name__ == '__main__':
	app.run(debug=True)

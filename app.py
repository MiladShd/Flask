from flask import Flask

app = Flask(__name__)


@app.route('/')

def hello():
	print("BBBBBsjsdf")
	return "hello Helllpoo"

if __name__ == '__main':
	app.run()
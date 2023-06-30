from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_World():
	return "Hello World"

@app.route('/name')
def namefunc():
	return "Lee yong-hwan"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port="9000")

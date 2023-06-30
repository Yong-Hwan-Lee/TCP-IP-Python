from flask import Flask, request, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

led_pin =18

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

@app.route('/')
def home():
	return "Hello Flask"

@app.route('/test')
def get():
	return render_template('get.html')

@app.route('/led/on')
def led_on():
	GPIO.output(led_pin, True)
	return "LED ON"

@app.route('/led/off')
def led_off() :
	GPIO.output(led_pin, False)
	return	"LED OFF"
	


@app.route('/post')
def post():
	return render_template('default.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', port = '8000', debug=True)

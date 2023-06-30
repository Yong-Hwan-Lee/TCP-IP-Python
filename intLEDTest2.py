import RPi.GPIO as GPIO
import  time

swPin = 24
LEDpin = 18
GPIO.setmode (GPIO.BCM) 
GPIO.setup (swPin, GPIO.IN)
GPIO.setup (LEDpin, GPIO.OUT)


def callbackfunc(channel):
	print("Interrupt !!")
	GPIO.output(LEDpin,False)
		
	

GPIO.add_event_detect(swPin, GPIO.RISING, callback=callbackfunc)
count = 0
try:
	while True:
		count = count + 1
		if (count%2) ==1:
			GPIO.output(LEDpin, True)
		elif (count%2)==0:
			GPIO.output(LEDpin, False)
		time.sleep(3)
except KeyboardInterrupt:
	GPIO.cleanup()

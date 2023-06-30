import RPi.GPIO as GPIO
import time
btnPin = 24
LED = 18

GPIO.setmode (GPIO.BCM) # GPIO.BOARD

GPIO.setup(btnPin, GPIO.IN)
count =0
while True:
	value = GPIO.input(24)
	if value ==True:
		count = count+1
		if(count % 16) == 10:
			print("A")
		elif(count % 16) == 11:
			print("B")
		elif(count % 16) == 12:
			print("C")
		elif(count%16) == 13:
			print("D")
		elif(count%16) == 14:
			print("E")
		elif(count%16) == 15:
			print("F")
		else:
			print(count%16)	
			
	time.sleep(0.1)

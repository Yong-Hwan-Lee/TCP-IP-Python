import RPi.GPIO as GPIO
import time

swPin = 24
LEDpin = 18
buzzerPin = 13
melody = [494, 294]
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)
buzz = GPIO.PWM(buzzerPin, 440)
GPIO.setup(swPin, GPIO.IN)
GPIO.setup(LEDpin, GPIO.OUT)

count = 0  

def callbackfunc(channel):
    global count  
    count += 1  
    print("Interrupt")

GPIO.add_event_detect(swPin, GPIO.RISING, callback=callbackfunc)

try:
    while True:
        if count % 2 == 1:
            while count % 2 == 1: 
                buzz.start(50)
                for i in range(len(melody)):
                    buzz.ChangeFrequency(melody[i])
                    time.sleep(0.5)
                GPIO.output(LEDpin, True)
                time.sleep(0.3)
                GPIO.output(LEDpin, False)
                time.sleep(0.3)
        else:
            buzz.stop()
            GPIO.output(LEDpin, False)
            time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()

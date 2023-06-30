import RPi.GPIO as GPIO
import time

swPin = 24
LEDpin = 18
buzzerPin = 13
melody = [220, 262]
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)
buzz = GPIO.PWM(buzzerPin, 440)
GPIO.setup(swPin, GPIO.IN)
GPIO.setup(LEDpin, GPIO.OUT)

is_running = False  # 동작 상태를 나타내는 변수

def callbackfunc(channel):
    global is_running
    if is_running:
        is_running = False
        buzz.stop()
        GPIO.output(LEDpin, False)
    else:
        is_running = True
        while is_running:
            buzz.start(50)
            for i in range(len(melody)):
                buzz.ChangeFrequency(melody[i])
                time.sleep(0.5)
            GPIO.output(LEDpin, True)
            time.sleep(0.3)
            GPIO.output(LEDpin, False)
            time.sleep(0.3)

            if not GPIO.input(swPin):  # 스위치가 눌렸을 때 while 문을 빠져나옴
                is_running = False
                buzz.stop()
                GPIO.output(LEDpin, False)
                break

GPIO.add_event_detect(swPin, GPIO.RISING, callback=callbackfunc, bouncetime=200)

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()

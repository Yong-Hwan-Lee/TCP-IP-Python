import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 17
ECHO= 27
GPIO.setup(TRIG, GPIO.OUT) #trig 초음파 신호 전송핀번호및 출력지정
GPIO.setup(ECHO, GPIO.IN) #echo 초음파 수신하는 수신핀 번호 지정및 입력지정

GPIO.output(TRIG,False)
print("초음파 출력 초기화")
time.sleep(2)

try:
	while True:
		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)

		while GPIO.input(ECHO) == 0:
				start = time.time()

		while GPIO.input(ECHO) ==1:
				stop = time.time()
		
		check_time = stop - start
		distance = check_time * 34300 /2
		print("Distance: %.1f cm "% distance)
		time.sleep(0.4)

except KeyboardInterrupt:
		GPIO.cleanup()
		print("bye~")

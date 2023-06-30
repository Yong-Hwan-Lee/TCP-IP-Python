import RPi.GPIO as GPIO
import time

buzzerPin = 13
melody = [196, 196, 220,220,196,196,165,165,196,196,165,165,147,147,147,147,196,196,220,220,196,196,165,165,196,165,147,165,131,131,131,131]
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)

buzz = GPIO.PWM(buzzerPin, 440) # 440Hz 를 갖는 객체 생성

try:
	while True:
		buzz.start(50)	# duty cycle 50으로 pwm출력시작
		for i in range(0, len(melody)):
			buzz.ChangeFrequency(melody[i]) # 주파수변경
			time.sleep(0.5)
		buzz.stop()		# pwm 종료
		time.sleep(1)

except KeyboardInterrupt: # 키보드 인터럽트
	GPIO.cleanup()

		


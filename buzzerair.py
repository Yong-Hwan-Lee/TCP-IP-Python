import RPi.GPIO as GPIO
import time


buzzerPin = 13
melody = [131, 147, 165, 175, 196, 220, 247, 262]
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)

buzz = GPIO.PWM(buzzerPin, 440)  # 440Hz를 갖는 객체 생성


try:
    while True:
            i = int(input())
            if i < 0 or i > len(melody):
                print("잘못된 입력입니다. ")
                continue
            buzz.ChangeFrequency(melody[i-1])  # 주파수 변경
            buzz.start(50)
            time.sleep(0.5)
            buzz.stop()
            time.sleep(0.1)

except KeyboardInterrupt:  # 키보드 인터럽트
    GPIO.cleanup()

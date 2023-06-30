import sys
import RPi.GPIO as GPIO
import time
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QThread, pyqtSignal


buzzerPin = 13
melody = [131, 147, 165, 175, 196, 220, 247, 262]
LEDpin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)
btnPin = 24
TRIG = 17
ECHO = 27
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
A = 7
B = 6
C = 4
D = 2
E = 1
F = 9
G = 10
GPIO.setwarnings(False)
GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
GPIO.setup(F, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)

def reset():
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, False)
    GPIO.output(F, False)
    GPIO.output(G, False)

def zero():
    GPIO.output(A, True)
    GPIO.output(B, True)
    GPIO.output(C, True)
    GPIO.output(D, True)
    GPIO.output(E, True)
    GPIO.output(F, True)

def one():
    GPIO.output(B, True)
    GPIO.output(C, True)

def two():
    GPIO.output(A, True)
    GPIO.output(B, True)
    GPIO.output(G, True)
    GPIO.output(E, True)
    GPIO.output(D, True)

def three():
    GPIO.output(A, True)
    GPIO.output(B, True)
    GPIO.output(C, True)
    GPIO.output(D, True)
    GPIO.output(G, True)

def four():
    GPIO.output(B, True)
    GPIO.output(C, True)
    GPIO.output(F, True)
    GPIO.output(G, True)

def five():
    GPIO.output(A, True)
    GPIO.output(F, True)
    GPIO.output(G, True)
    GPIO.output(C, True)
    GPIO.output(D, True)

def six():
    GPIO.output(A, True)
    GPIO.output(F, True)
    GPIO.output(E, True)
    GPIO.output(G, True)
    GPIO.output(C, True)
    GPIO.output(D, True)

def seven():
    GPIO.output(A, True)
    GPIO.output(B, True)
    GPIO.output(C, True)

def eight():
    GPIO.output(A, True)
    GPIO.output(B, True)
    GPIO.output(C, True)
    GPIO.output(D, True)
    GPIO.output(E, True)
    GPIO.output(F, True)
    GPIO.output(G, True)

def nine():
    GPIO.output(A, True)
    GPIO.output(B, True)
    GPIO.output(C, True)
    GPIO.output(D, True)
    GPIO.output(G, True)
    GPIO.output(F, True)

def a():
    GPIO.output(A, True)
    GPIO.output(B, True)
    GPIO.output(C, True)
    GPIO.output(E, True)
    GPIO.output(F, True)
    GPIO.output(G, True)

def b():
    GPIO.output(F, True)
    GPIO.output(G, True)
    GPIO.output(E, True)
    GPIO.output(C, True)
    GPIO.output(D, True)

def c():
    GPIO.output(A, True)
    GPIO.output(F, True)
    GPIO.output(E, True)
    GPIO.output(D, True)

def d():
    GPIO.output(B, True)
    GPIO.output(C, True)
    GPIO.output(G, True)
    GPIO.output(E, True)
    GPIO.output(D, True)

def e():
    GPIO.output(A, True)
    GPIO.output(G, True)
    GPIO.output(F, True)
    GPIO.output(E, True)
    GPIO.output(D, True)

def f():
    GPIO.output(A, True)
    GPIO.output(F, True)
    GPIO.output(G, True)
    GPIO.output(E, True)

list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "a", "b", "c", "d", "e", "f"]

buzz = GPIO.PWM(buzzerPin, 440)
GPIO.setup(LEDpin, GPIO.OUT)

class qtApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Python/env/Src/App.ui', self)
        self.btnLEDON.clicked.connect(self.btnLEDONClicked)
        self.btnLEDOFF.clicked.connect(self.btnLEDOFFClicked)
        self.btnSdON.clicked.connect(self.btnSdONClicked)
        self.btnSnON.clicked.connect(self.btnSnONClicked)
        self.LbUs.setText("Distance: N/A cm")  # 초기 텍스트 설정
        self.cbNum.currentIndexChanged.connect(self.cbNumchanged)

    def btnLEDONClicked(self):
        GPIO.output(LEDpin, True)

    def btnLEDOFFClicked(self):
        GPIO.output(LEDpin, False)

    def btnSdONClicked(self):
        buzz.start(50)
        for i in range(0, len(melody)):
            buzz.ChangeFrequency(melody[i])
            time.sleep(0.5)
        buzz.stop()

    def btnSnONClicked(self):
        self.UltraSonicThread = UltraSonicThread(self)  # 초음파 스레드 생성
        self.UltraSonicThread.distanceChanged.connect(self.updateDistance)  # 거리 변경 시그널 연결
        self.UltraSonicThread.start()  # 초음파 스레드 시작

    def updateDistance(self, distance):
        self.LbUs.setText("Distance: %.1f cm" % distance)

    def closeEvent(self, event):
        # 윈도우를 닫을 때 GPIO 설정 초기화
        GPIO.cleanup()

    def cbNumchanged(self, index):
        reset()
        i = self.cbNum.currentIndex()
        globals()[list[i]]()
        


class UltraSonicThread(QThread):
    distanceChanged = pyqtSignal(float)  # 거리 변경 시그널

    def run(self):
        while True:
            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)
            while GPIO.input(ECHO) == 0:
                start = time.time()
            while GPIO.input(ECHO) == 1:
                stop = time.time()
            check_time = stop - start
            distance = check_time * 34300 / 2
            self.distanceChanged.emit(distance)  # 거리 변경 시그널 발생
            time.sleep(0.4)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())
import RPi.GPIO as GPIO
import time
A = 7
B = 6
C = 4
D = 2
E = 1
F = 9
G = 10
GPIO.setmode(GPIO.BCM)
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


while True:
	for i in range(16):
		reset()
		globals()[list[i]]()
		time.sleep(1)

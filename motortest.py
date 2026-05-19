import RPi.GPIO as GPIO
import time

STEP = 23
DIR = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)

GPIO.output(DIR, GPIO.HIGH)

print("Motor test starting...")

for i in range(2000):
    GPIO.output(STEP, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(STEP, GPIO.LOW)
    time.sleep(0.001)

print("Done")

GPIO.cleanup()
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.HIGH)
print('turned on')
time.sleep(0.5)
print('turn off')
GPIO.output(18, GPIO.LOW)

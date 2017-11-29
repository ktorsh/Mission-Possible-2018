import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.IN)
for i in range(100):
    print(GPIO.input(5))
    


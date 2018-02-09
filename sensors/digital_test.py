import RPi.GPIO as GPIO

lpin=11
GPIO.setmode(GPIO.BCM)
GPIO.setup(lpin, GPIO.OUT)
GPIO.output(lpin, 1)

rpin=13
GPIO.setup(rpin, GPIO.OUT)
GPIO.output(rpin, 1)

while True:
    if (GPIO.input(rpin)==0):
        print "Pressed"


import RPi.GPIO as GPIO
rover = Adafruit_MotorHAT(addr=0x60)

lpin=11
GPIO.setmode(GPIO.BCM)
GPIO.setup(lpin, GPIO.OUT)
GPIO.output(lpin, 1)

rpin=13
GPIO.setup(rpin, GPIO.OUT)
GPIO.output(rpin, 1)

while True:
    print("Left: "+GPIO.input(lpin))
    print("Right: "+GPIO.input(rpin))

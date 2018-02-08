import RPi.GPIO as GPIO
rover = Adafruit_MotorHAT(addr=0x60)

lpin=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(lpin, GPIO.OUT)
GPIO.output(lpin, 1)

rpin=17
GPIO.setup(rpin, GPIO.OUT)
GPIO.output(rpin, 1)

leftm=rover.getMotor(1)#left motor
leftm.setSpeed(255)

rightm=rover.getMotor(2)#right motor
rightm.setSpeed(255)

def forward():
    leftm.run(Adafruit_MotorHAT.FORWARD)
    rightm.run(Adafruit_MotorHAT.FORWARD)
    
def backward():
    leftm.run(Adafruit_MotorHAT.BACKWARD)
    rightm.run(Adafruit_MotorHAT.BACKWARD)

def right():
    leftm.run(Adafruit_MotorHAT.FORWARD)
    rightm.run(Adafruit_MotorHAT.BACKWARD)

def left():
    leftm.run(Adafruit_MotorHAT.BACKWARD)
    rightm.run(Adafruit_MotorHAT.FORWARD)

def stop():
    leftm.run(Adafruit_MotorHAT.RELEASE)
    rightm.run(Adafruit_MotorHAT.RELEASE)

try:
    while True:
        if !(GPIO.input(lpin)):
            backward()
            time.sleep(1.5)
            right()
            time.sleep(3)
        elif !(GPIO.input(rpin)):
            backward()
            time.sleep(1.5)
            left()
            time.sleep(3)
        forward()
except KeyboardInterrupt:
    GPIO.cleanup()


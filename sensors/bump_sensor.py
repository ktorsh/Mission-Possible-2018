import sys
sys.path.append("/home/ktorsh/Documents/Adafruit-Motor-HAT-Python-Library")
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time
import RPi.GPIO as GPIO
rover = Adafruit_MotorHAT(addr=0x60)


leftm=rover.getMotor(1)#left motor
leftm.setSpeed(255)

rightm=rover.getMotor(2)#right motor
rightm.setSpeed(255)

ser=serial.Serial("/dev/ttyACM0",9600)
#ser=serial.Serial("dev/ttyACM1",9600)
def getLastLine():
    lines=ser.read(ser.inWaiting()).split("\n")
    return (lines[-2])
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
        lines=getLastLine().split(",")
        if lines[3]=="0":
            backward()
            time.sleep(1.5)
            right()
            time.sleep(3)
        elif lines[4]=="0":
            backward()
            time.sleep(1.5)
            left()
            time.sleep(3)
        forward()
except KeyboardInterrupt:
    GPIO.cleanup()


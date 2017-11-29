import sys
sys.path.append("/home/pi/Adafruit-Motor-HAT-Python-Library")
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time
import atexit

rover = Adafruit_MotorHAT(addr=0x60)

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
forward()




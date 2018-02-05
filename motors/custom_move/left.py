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

length=float(input("Length of Action: "))

leftm.run(Adafruit_MotorHAT.BACKWARD)
rightm.run(Adafruit_MotorHAT.FORWARD)

time.sleep(length)

leftm.run(Adafruit_MotorHAT.RELEASE)
rightm.run(Adafruit_MotorHAT.RELEASE)

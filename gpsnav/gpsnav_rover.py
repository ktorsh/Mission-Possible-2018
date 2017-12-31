"""
Rover GPS Navigation Challenge
Group Y1: Kasra T, Roshini P, Shabarish N, Sanjana K.
Purpose: Using the arctan method. it allows the rover to navigate to a desired location regardless of position
"""

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time
import atexit
import math

rover = Adafruit_MotorHAT(addr=0x60)

leftm=rover.getMotor(1)#left motor
leftm.setSpeed(150)

rightm=rover.getMotor(2)#right motor
rightm.setSpeed(150)

def heading(start, end): #returns the angle of the vector with respect to the relative x-axis
    dx=end[0]-start[0]
    dy=end[1]-start[1]
    if dx==0 and dy>0: #to prevent undefined division in dy/dx
        return 90
    if dx==0 and dy<0:
        return 270
    if dx<0:
        return 180+(math.atan(dy/dx)*180/math.pi)
    else:
        return (math.atan(dy/dx)*180/math.pi)%360

def forward(time_length):
    leftm.run(Adafruit_MotorHAT.FORWARD)
    rightm.run(Adafruit_MotorHAT.FORWARD)
    
def backward(time_length):
    leftm.run(Adafruit_MotorHAT.BACKWARD)
    rightm.run(Adafruit_MotorHAT.BACKWARD)

def right(degrees):
    leftm.run(Adafruit_MotorHAT.FORWARD)
    rightm.run(Adafruit_MotorHAT.BACKWARD)

def left(degrees):
    leftm.run(Adafruit_MotorHAT.BACKWARD)
    rightm.run(Adafruit_MotorHAT.FORWARD)

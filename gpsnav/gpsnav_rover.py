"""
Rover GPS Navigation Challenge
Group Y1: Kasra T, Roshini P, Shabarish N, Sanjana K.
Purpose: Using the arctan method. it allows the rover to navigate to a desired location regardless of position
Note: angles are in radians, might be converted to degrees in the future
"""
import sys
sys.path.append("/home/ktorsh/Documents/Adafruit-Motor-HAT-Python-Library")
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time
import atexit
import math
import urllib2

SEC_TO_RADIAN=2.41 #amount of seconds it takes for the rover to turn one radian *NOT ACTUAL VALUE
time_delta=4 #time in seconds for the rover to update its current location *NOT ACTUAL VALUE
length_delta=200 #how close the rover has to be of the desingnated point *NOT ACTUAL VALUE
target=(500,500) #desired cordinated location *NOT ACTUAL VALUE

rover = Adafruit_MotorHAT(addr=0x60)

leftm=rover.getMotor(1)#left motor
leftm.setSpeed(255)

rightm=rover.getMotor(2)#right motor
rightm.setSpeed(255)

def getCord():
    cords=urllib2.urlopen("http://10.144.7.184/coord.txt").read()
    clist=cords.split(",")
    return (int(clist[0]),int(clist[1]))

def heading(start, end): #returns the angle of the vector with respect to the relative x-axis
    dx=end[0]-start[0]
    dy=end[1]-start[1] 
    if dx==0 and dy>0: #to prevent undefined division in dy/dx
        return math.pi/2
    if dx==0 and dy<0:
        return 3*math.pi/2
    if dx<0:#if dx<0 you have to had pi/2 to get the actual angle position
        return math.pi+math.atan(dy/dx)
    else:
        return (math.atan(dy/dx))%(2*math.pi) #if the vector is in quadrant IV, it will loop from a negative angle to its corresponding positive angle

def forward(time_length):
    leftm.run(Adafruit_MotorHAT.FORWARD)
    rightm.run(Adafruit_MotorHAT.FORWARD)
    time.sleep(time_length)
    
def backward(time_length):
    leftm.run(Adafruit_MotorHAT.BACKWARD)
    rightm.run(Adafruit_MotorHAT.BACKWARD)
    time.sleep(time_length)

def right(radians):
    leftm.run(Adafruit_MotorHAT.FORWARD)
    rightm.run(Adafruit_MotorHAT.BACKWARD)
    time.sleep(radians*SEC_TO_RADIAN)

def left(radians):
    leftm.run(Adafruit_MotorHAT.BACKWARD)
    rightm.run(Adafruit_MotorHAT.FORWARD)
    time.sleep(radians*SEC_TO_RADIAN)
def stop():
    leftm.run(Adafruit_MotorHAT.RELEASE)
    rightm.run(Adafruit_MotorHAT.RELEASE)

start=getCord()
#continue the following loop until your x and y are both within "delta" of the target
while not(target[0] - length_delta <= start[0] <= target[0] + length_delta) or not(target[1] - length_delta <= start[1] <= target[1] + length_delta):
    forward(time_delta)
    stop()
    time.sleep(6)
    end=getCord()#not yet defined
    if (start!=end):
        turn_angle=(heading(end,target)-heading(start,end))%(2*math.pi)
        if 0<=turn_angle<=math.pi:
            left(turn_angle)
        else:
            right(2*math.pi-turn_angle)
    start=getCord()#not yet defined
stop()

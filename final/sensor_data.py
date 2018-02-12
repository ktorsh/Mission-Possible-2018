#!/usr/bin/python
import smbus
import math
import os
import serial
import urllib2

power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

bus = smbus.SMBus(1) 
address = 0x68       # This is the address value read via the i2cdetect command

# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)

ser=serial.Serial("/dev/ttyACM0",9600)
#ser=serial.Serial("dev/ttyACM1",9600)

def getCord():
    cords=urllib2.urlopen("http://10.144.7.183/coord.txt").read()
    clist=cords.split(",")
    return (int(clist[0]),int(clist[1]))

def getLastLine():
    lines=ser.read(ser.inWaiting()).split("\n")
    return (lines[-2])

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val
 
def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))
 
def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)
 
def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

cords=getCord()
print(ser.readline())
data=getLastLine().split(",")
print("Hall Effect Sensor: "+data[0])
print("Temperature in C: "+data[1])
print("Gas Sensor: "+data[2])

accel_xout = read_word_2c(0x3b)
accel_yout = read_word_2c(0x3d)
accel_zout = read_word_2c(0x3f) 

accel_xout_scaled = accel_xout / 16384.0
accel_yout_scaled = accel_yout / 16384.0
accel_zout_scaled = accel_zout / 16384.0

x_rot=get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
y_rot=get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)

print("x rotation: " + str(x_rot))
print("y rotation: " + str(y_rot))

message=str(raw_input("Message with report: "))

with open('collected_sensor_data/sensor_data.txt', 'a') as datas:
    datas.write("Cordinates: "+str(cords)+"\n")
    datas.write("Hall Effect Sensor: "+data[0]+"\n")
    datas.write("Temperature in C: "+data[1]+"\n")
    datas.write("Gas Sensor: "+data[2]+"\n")
    datas.write("X rotation: " + str(x_rot)+"\n")
    datas.write("Y rotation: " + str(y_rot)+"\n")
    datas.write("Driver Message: "+message+"\n")
    datas.write(" \n")
    

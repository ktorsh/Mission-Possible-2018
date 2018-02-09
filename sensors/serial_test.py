import os
import serial

ser=serial.Serial("/dev/ttyACM0",9600)
#ser=serial.Serial("dev/ttyACM1",9600)
print(ser.read())
def getLastLine():
    print(ser.read(ser.inWaiting())
    lines=ser.read(ser.inWaiting()).split("\n")
    return (lines[-2])

data=getLastLine().split(",")
print("Hall Effect Sensor: "+data[0])
print("Temperature in C: "+data[1])
print("Gas Sensor: "+data[2])



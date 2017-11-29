import os
import serial

ser=serial.Serial("/dev/ttyACM0",9600)
#ser=serial.Serial("dev/ttyACM1",9600)

def getLastLine():
    lines=ser.read(ser.inWaiting()).split("\n")
    return (lines[-2])
user_input=""
while user_input!="quit":
    user_input=raw_input("E: ")
    ser.flush()
    data=ser.readline()
    print(getLastLine())

import os
import serial

ser=serial.Serial("dev/ttyACM0",9600)
#ser=serial.Serial("dev/ttyACM1",9600)
user_input=""
while user_input!="quit":
    user_input=str(input())
    data=ser.readline()
    print(data)

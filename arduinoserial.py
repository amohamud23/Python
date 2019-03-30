import serial                                                              #Serial imported for Serial communication
import time                                                                #Required to use delay functions
Arduino = serial.Serial(post='/dev/cu.usbserial-A103TJ69',baudrate=9600)          #Create Serial port object called ArduinoUnoSerialData time.sleep(2)                                                             #wait for 2 secounds for the communication to get established
Arduino.write('s'.encode())

print(Arduino.readline())

Arduino.write("Hello")
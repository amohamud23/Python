import PyLidar3
import json
import pptk
import numpy
import time # Time module
#Serial port to which lidar connected, Get it from device manager windows
#In linux type in terminal -- ls /dev/tty* 
#port = input("Enter port name which lidar is connected:") #windows
port = "/dev/tty.SLAB_USBtoUART" #linux
Obj = PyLidar3.YdLidarX4(port) #PyLidar3.your_version_of_lidar(port,chunk_size) 
if(Obj.Connect()):
    print(Obj.GetDeviceInfo())
    gen = Obj.StartScanning()
    t = time.time() # start time 
    table = []
    i = 0
    while (time.time() - t) < 30: #scan for 30 seconds
        print(next(gen))
        dic = next(gen)
        for angle, distance in dic.items():
            x = numpy.math.cos(numpy.math.radians(angle))*(distance/1000)
            y = numpy.math.sin(numpy.math.radians(angle))*(distance/1000)
        
            #print(x, " ", y)
            #print(angle, " ", distance)
            table.append([x,y,0])

        time.sleep(0.5)
    Obj.StopScanning()
    Obj.Disconnect()
    #print(table)
    v = pptk.viewer(table)
    v.set(point_size=0.01)
else:
    print("Error connecting to device")

    
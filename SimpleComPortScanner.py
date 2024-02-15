# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:13:54 2024

@author: JGarner
"""

import serial.tools.list_ports
import serial
import time
import numpy as np

arduinoHWID = 'VID:PID=2341:8037'
TeensyHWID  = 'VID:PID=16C0:0483'
ESP32HWID = 'VID:PID=10C4:EA60'

ports_av = serial.tools.list_ports.comports()

ser = serial.Serial()

x = np.arange(stop, )

startTime = int(time.time() * 1000)



'''
for i in ports_av:
    print("NEW DEVICE!!")
    print(i.device)
    print(i.description)
    #print(i.pid)
    #print(i.vid)
    print(i.hwid)
    if ESP32HWID in i.hwid:
        print("Found ESP32")
        ser = serial.Serial(i.device)
        print(ser)
        if ser.is_open:
            ser.close()
        ser.open()
        if ser.is_open:
            print("Openned serial port")
            print(ser)
            ser.close()

'''
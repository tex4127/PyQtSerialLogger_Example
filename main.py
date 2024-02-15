# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 14:22:50 2024

@author: JGarner
"""


from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtSerialPort
from PyQt5.QtCore import QIODevice
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
import serial.tools.list_ports
import plotGenerator as pg
from LoggerWindwo import Ui_MainWindow
import sys
import time
from datetime import datetime
import csv

arduinoHWID = 'VID:PID=2341:8037'
TeensyHWID  = 'VID:PID=16C0:0483'
ESP32HWID = 'VID:PID=10C4:EA60'

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
         
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.serialPort = QSerialPort()
        self.connectedDeviceType = ''
        #for the sake of testing the plot, lets make a default plot to show
        self.plotNames = ['xPlot.png', 'yPlot.png', 'zPlot.png']
        pg.generatePlot(0, 0, 'x Values', self.plotNames[0], 20, 50, 'magenta')
        
        self.logFileName = "data.csv"
        self.ui.lineEdit_logFileName.setText(self.logFileName)
        ''' Program Static Staring Variables '''
        self.plotPixMap = QPixmap(self.plotNames[0])
        self.ui.label_imagePlot.setPixmap(self.plotPixMap)
        
        ''' Attach Signals '''
        self.ui.pushButton_selectFile.clicked.connect(self.ButtonSetFile_ClickEvent)
        self.ui.pushButton_ConnectToSerial.clicked.connect(self.openSerialPort)
        
    #updates the plot to better represent the current data sets    
    def updatePlot(self):
        self.plotPixMap(self.plotNames[0])
        self.ui.label_imagePlot.setPixmap(self.plotPixMap)
     
    def ButtonSetFile_ClickEvent(self):
        #open a file dialog with save options
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(self, 'Select File', "", 'CSV (*.csv)')
        if filename and not(filename in self.logFileName):
            self.logFileName = filename
            self.ui.lineEdit_logFileName.setText(self.logFileName)
            self.writeHeaderToFile()
    
    def findMicroController(self):
        ports_av = list(serial.tools.list_ports.comports())
        for p in ports_av:
            if arduinoHWID in p.hwid:
                self.connectedDeviceType = 'Arduino'
                print(self.connectedDeviceType)
                return p.name
            if TeensyHWID in p.hwid:
                self.connectedDeviceType = 'Teensy 4.1'
                print(self.connectedDeviceType)
                return p.name
            if ESP32HWID in p.hwid:
                self.connectedDeviceType = 'ESP32'
                print(self.connectedDeviceType)
                return p.name
    
    def openSerialPort(self):
        #first we need to scan for all available ports
        port = self.findMicroController()
        print(port)
        self.serialPort.setPortName(port)
        print(self.serialPort.portName)
        self.serialPort.setBaudRate(QSerialPort.Baud115200)
        self.serialPort.setParity(QSerialPort.NoParity)
        self.serialPort.setDataBits(QSerialPort.Data8)
        self.serialPort.setStopBits(QSerialPort.OneStop)
        self.serialPort.setFlowControl(QSerialPort.NoFlowControl)
        if self.serialPort.open(QSerialPort.ReadWrite):
            print(self.serialPort)
            print("Connected")
            return
        else:
            print(self.serialPort.errorString())
        print("Did not connect: ", self.serialPort)

    def writeHeaderToFile(self):
        with open(self.logFileName, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(list(('x','y','z','time')))
            file.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    app.exec()
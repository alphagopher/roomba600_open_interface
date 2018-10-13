import sys
import serial
import time
import datetime
import math

class SerialReceiver:
    def __init__(self, PORT, BAUD_RATE=115200):
        print('PORT is', PORT)
        if type(PORT) == type('string'):
            if PORT == 'sim':
                print('In simulated mode...')
                self.ser = 'sim' # SRSerial('mapSquare.txt')
            else:
                # for Mac/Linux - use whole port name
                # print 'In Mac/Linux mode...'
                self.ser = serial.Serial(PORT, baudrate=BAUD_RATE, timeout=0.5)
        # otherwise, we try to open the numeric serial port...
        else:
            # print 'In Windows mode...'
            self.ser = serial.Serial(PORT-1, baudrate=BAUD_RATE, timeout=0.5)
        # did the serial port actually open?
        if self.ser != 'sim' and self.ser.isOpen():
            print('Serial port did open, presumably to a roomba...')
        else:
            print('Serial port did NOT open, check the')
            print('  - port number')
            print('  - physical connection')
            print('  - baud rate of the roomba (it\'s _possible_, if unlikely,')
            print('              that it might be set to 19200 instead')
            print('              of the default 57600 - removing and')
            print('              reinstalling the battery should reset it.')


        # self.ser = serial.Serial(PORT-1, baudrate=BAUD_RATE, timeout=0.5)


    def sendToDevice(self, command):
        self.ser.write(command.getByteArray())
        pass

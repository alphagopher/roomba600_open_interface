import roomba_command
import sys
import serial
import time
import datetime
import math

START_OI = roomba_command.RoombaCommand("START_OI", 128, [])
STOP_OI = roomba_command.RoombaCommand("STOP_OI", 173, [])
SAFE_MODE = roomba_command.RoombaCommand("SAFE_MODE", 131, [])
FULL_MODE = roomba_command.RoombaCommand("FULL_MODE", 132, [])
DRIVE = roomba_command.RoombaCommand("DRIVE", 137, [])
BRUSHES_ON = roomba_command.RoombaCommand("BRUSHES_ON", 144, [100, 100, 100])
BRUSHES_OFF = roomba_command.RoombaCommand("BRUSHES_OFF", 144, [0, 0, 0])
WHEEL_SPAN = 235.0

class SerialConnection:
    def __init__(self, PORT, BAUD_RATE=115200):
        """ the constructor which tries to open the
        connection to the robot at port PORT
        """
        _debug = False
        # to do: find the shortest safe serial timeout value...
        # to do: use the timeout to do more error checking than
        #        is currently done...
        #
        # the -1 here is because windows starts counting from 1
        # in the hardware control panel, but not in pyserial, it seems
        
        # if PORT is the string 'simulated' (or any string for the moment)
        # we use our SRSerial class
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

        self.__sendCommand(START_OI) 
        print('Putting the robot into safe mode...')
        self.__sendCommand(SAFE_MODE) 

    _debug = True

    def __sendCommand(self, command, delaySeconds=0.2):
        # Roomba needs literal commands to be sent as ser.write([0x80, 0xFF, etc.])
        if self._debug==True:
            print(datetime.datetime.now(), " ", sys._getframe(0).f_code.co_name, " ", command.commandName, " ", command.opCode, " ", command.dataBytes)
            self.ser.write(command.getByteArray())
        
        if command == SAFE_MODE or command == FULL_MODE or command == START_OI or command == STOP_OI:
            time.sleep(delaySeconds)

    def __go(self, cm_per_sec=0, deg_per_sec=0):
        # need to convert to the roomba's drive parameters
        #
        # for now, just one or the other...
        if cm_per_sec == 0:
            # just handle rotation
            # convert to radians
            rad_per_sec = math.radians(deg_per_sec)
            # make sure the direction is correct
            if rad_per_sec >= 0:  dirstr = 'CCW'
            else: dirstr = 'CW'
            # compute the velocity, given that the robot's
            # radius is 258mm/2.0
            vel_mm_sec = math.fabs(rad_per_sec) * (WHEEL_SPAN/2.0)
            # send it off to the robot
            self.__drive( vel_mm_sec, 0, dirstr )
        
        elif deg_per_sec == 0:
            # just handle forward/backward translation
            vel_mm_sec = 10.0*cm_per_sec
            big_radius = 32767
            # send it off to the robot
            self.__drive( vel_mm_sec, big_radius )
        
        else:
            # move in the appropriate arc
            rad_per_sec = math.radians(deg_per_sec)
            vel_mm_sec = 10.0*cm_per_sec
            radius_mm = vel_mm_sec / rad_per_sec
            # check for extremes
            if radius_mm > 32767: radius_mm = 32767
            if radius_mm < -32767: radius_mm = -32767
            self.__drive( vel_mm_sec, radius_mm )
        
        return

    def __drive(self, roomba_mm_sec, roomba_radius_mm, turn_dir='CCW'):
        # first, they should be ints
        #   in case they're being generated mathematically
        if type(roomba_mm_sec) != type(42):
            roomba_mm_sec = int(roomba_mm_sec)
        if type(roomba_radius_mm) != type(42):
            roomba_radius_mm = int(roomba_radius_mm)
        
        # we check that the inputs are within limits
        # if not, we cap them there
        if roomba_mm_sec < -500:
            roomba_mm_sec = -500
        if roomba_mm_sec > 500:
            roomba_mm_sec = 500
        
        # if the radius is beyond the limits, we go straight
        # it doesn't really seem to go straight, however...
        if roomba_radius_mm < -2000:
            roomba_radius_mm = 32768
        if roomba_radius_mm > 2000:
            roomba_radius_mm = 32768        
        # get the two bytes from the velocity
        # these come back as numbers, so we will chr them
        velHighVal, velLowVal = self.__toTwosComplement2Bytes( roomba_mm_sec )
        
        # get the two bytes from the radius in the same way
        # note the special cases
        if roomba_radius_mm == 0:
            if turn_dir == 'CW':
                roomba_radius_mm = -1
            else: # default is 'CCW' (turning left)
                roomba_radius_mm = 1
        radiusHighVal, radiusLowVal = self.__toTwosComplement2Bytes( roomba_radius_mm )
        
        #print 'bytes are', velHighVal, velLowVal, radiusHighVal, radiusLowVal
        
        # send these bytes and set the stored velocities
        tmpCommand = DRIVE
        tmpCommand.dataBytes = [velHighVal, velLowVal, radiusHighVal, radiusLowVal]
        self.__sendCommand(tmpCommand)
        #self.__sendCommand( velHighVal )
        #self.__sendCommand( velLowVal )
        #self.__sendCommand( radiusHighVal )
        #self.__sendCommand( radiusLowVal )

    def __toTwosComplement2Bytes(self, value):

        # returns two bytes (ints) in high, low order
        # whose bits form the input value when interpreted in
        # two's complement

        # if positive or zero, it's OK
        if value >= 0:
            eqBitVal = value
        # if it's negative, I think it is this
        else:
            eqBitVal = (1<<16) + value
        
        return ( (eqBitVal >> 8) & 0xFF, eqBitVal & 0xFF )

    def connect(self):
        self.__sendCommand(START_OI)
        self.__sendCommand(SAFE_MODE)
        return

    def toSafeMode(self):
        # Send STOP_OI command, close serial connection
        self.__sendCommand(START_OI)
        self.__sendCommand(SAFE_MODE)
        # self.ser.close()
        return

    def toFullMode(self):
        # Send STOP_OI command, close serial connection
        self.__sendCommand(START_OI)
        self.__sendCommand(FULL_MODE)
        # self.ser.close()
        return

    def shutDown(self):
        # Send STOP_OI command, close serial connection
        self.__sendCommand(STOP_OI)
        # self.ser.close()
        return

    def moveForward(self):
        print("Sending command - ")
        self.__go(30,0)
        time.sleep(0.5)
        self.__go(0,0)
        return
    
    def moveBackward(self):
        self.__go(-30,0)
        time.sleep(0.5)
        self.__go(0,0)
        return

    def turnLeft(self):
        self.__go(0,100)
        time.sleep(0.5)
        self.__go(0,0)
        return
    
    def turnRight(self):
        self.__go(0,-100)
        time.sleep(0.5)
        self.__go(0,0)
        return

    def brushesOn(self):
        # Send STOP_OI command, close serial connection
        self.__sendCommand(BRUSHES_ON)
        # self.ser.close()
        return

    def brushesOff(self):
        # Send STOP_OI command, close serial connection
        self.__sendCommand(BRUSHES_OFF)
        # self.ser.close()
        return
import serial

class RoombaSerialConnection:
    def __init__(self, PORT, BAUD_RATE=115200):
        self.ser = serial.Serial(PORT, baudrate=BAUD_RATE, timeout=0.5)

        if self.ser.isOpen():
            print("Opened Serial Port on", PORT)
        else:
            print("Could not open serial port", PORT)

    def sendToDevice(self, command):
        self.ser.write(command.getByteArray())

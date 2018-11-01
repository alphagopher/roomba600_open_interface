import serial
import time

class RoombaSerialConnection:
    def __init__(self, PORT, BAUD_RATE=115200):
        self.ser = serial.Serial(PORT, baudrate=BAUD_RATE, timeout=0.5)

        if self.ser.isOpen():
            print("Opened Serial Port on", PORT)
        else:
            print("Could not open serial port", PORT)

    def close(self):
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        self.ser.close()

    def sendToDevice(self, command):
        try:
            print("Executing Command - ", command.commandName + " " + str(command.getIntArray()))
            self.ser.reset_input_buffer()
            self.ser.write(command.getByteArray())

            if(len(command.sensorPackets) > 0):
                print("-----Reading Buffer for Input Commands-----")
                for sensorPacket in command.sensorPackets:
                    time.sleep(.15)
                    print("Sensor Packet - ", sensorPacket.toLogString(), "[Input Buffer Size.. ", self.ser.in_waiting, "...Reading...", sensorPacket.dataBytesReturned)
                    
                    sensorPacket.responseBytes = self.ser.read(sensorPacket.dataBytesReturned)

                    print("Sensor Reading: ", int.from_bytes(sensorPacket.responseBytes, byteorder='big', signed=sensorPacket.signed))
        except Exception as e: 
            print(e)
            self.ser.reset_input_buffer()
                

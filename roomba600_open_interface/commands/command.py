class Command():
    """
    Declare an interface for executing an operation.
    """
    def __init__(self, receiver):
        self._receiver = receiver
        self.commandName = ""
        self.opCode = 0
        self.dataBytes = []
        self.dataBytesRequiredLength = 0
        self.sensorPackets = []
        self.sensorPacketsRequiredLength = 0

    def isValid(self):
        return (len(self.dataBytes) == self.dataBytesRequiredLength and len(self.sensorPackets) == self.sensorPacketsRequiredLength) 

    def getByteArray(self):
        #TODO: Fix this so it works for more than one Sensor Packet 
        sensorPacketByteArray = []
        if(len(self.sensorPackets) > 0):
            sensorPacketByteArray = [self.sensorPackets[0].packetId]

        return bytes([self.opCode] + self.dataBytes + sensorPacketByteArray)

    def getIntArray(self):
        sensorPacketIntArray = []
        for sensorPacket in self.sensorPackets:
            sensorPacketIntArray += sensorPacket.getIntArray()

        return [self.opCode] + self.dataBytes + sensorPacketIntArray

    def execute(self):
        #TODO: bubble up sensor packet results or return code?
        self._receiver.sendToDevice(self)

    def toLogString(self):
        return self.commandName + " Opcode: " + str(self.opCode) + " dataBytes: " + str(self.dataBytes) + " dataBytesRequiredLength: " + str(self.dataBytesRequiredLength) + " sensorPacketsRequiredLength: " + str(self.sensorPacketsRequiredLength)
class RoombaCommand:
    def __init__(self, commandName, opCode, dataBytes):
        self.commandName = commandName
        self.opCode = opCode
        self.dataBytes = dataBytes

    def getByteArray(self):
        return bytes([self.opCode] + self.dataBytes)
     

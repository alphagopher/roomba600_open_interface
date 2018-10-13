class Packet:
    def __init__(self, packetName, packetId, dataBytes):
        self.packetName = packetName
        self.packetId = packetId
        self.dataBytes = dataBytes

    def getByteArray(self):
        return bytes(self.dataBytes)
     

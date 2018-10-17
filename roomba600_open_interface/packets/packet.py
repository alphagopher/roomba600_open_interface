class Packet:
    def __init__(self, packetName, packetId, dataBytes):
        self.packetId = packetId
        self.packetName = packetName
        self.dataBytes = dataBytes

    def getByteArray(self):
        return bytes(self.dataBytes)
     

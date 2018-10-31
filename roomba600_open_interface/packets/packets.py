class SensorPacket:
    def __init__(self, packetName, packetId):
        self.packetId = packetId
        self.packetName = packetName
        self.dataBytesReturned = 0
        self.signed = False

    def getIntArray(self):
        return [self.packetId]

    def getByteArray(self):
        return [bytes(self.packetId)]

    def toLogString(self):
        return str(self.packetName) + " " + str(self.packetId) + " dataBytes: " + str(self.dataBytesReturned) + " signed: " + str(self.signed)      

class ChargingStateSensorPacket(SensorPacket):
    def __init__(self):
        self.packetName = "ChargingStateSensorPacket"
        self.packetId = 21
        self.dataBytesReturned = 1
        self.signed = False

class BatteryChargeSensorPacket(SensorPacket):
    def __init__(self):
        self.packetName = "BatteryChargeSensorPacket"
        self.packetId = 25
        self.dataBytesReturned = 2
        self.signed = False    

class BatteryCapacitySensorPacket(SensorPacket):
    def __init__(self):
        self.packetName = "BatteryCapacitySensorPacket"
        self.packetId = 26
        self.dataBytesReturned = 2
        self.signed = False    

class OpenInterfaceModeSensorPacket(SensorPacket):
    def __init__(self):
        self.packetName = "OpenInterfaceModeSensorPacket"
        self.packetId = 35
        self.dataBytesReturned = 1
        self.signed = False



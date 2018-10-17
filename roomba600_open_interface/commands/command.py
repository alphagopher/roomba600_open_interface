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

    def isValid(self):
        return (len(self.dataBytes) == self.dataBytesRequiredLength)

    def getByteArray(self):
        return bytes([self.opCode] + self.dataBytes)

    def execute(self):
        self._receiver.sendToDevice(self)

    def toLogString(self):
        return self.commandName + " Opcode: " + str(self.opCode) + " dataBytes: " + str(self.dataBytes) + " dataBytesRequiredLength: " + str(self.dataBytesRequiredLength)
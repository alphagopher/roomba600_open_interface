class Command():
    """
    Declare an interface for executing an operation.
    """
    def __init__(self, receiver):
        self._receiver = receiver
        self.commandName = ""
        self.opCode = 0
        self.dataBytes = []

    def getByteArray(self):
        return bytes([self.opCode] + self.dataBytes)

    def execute(self):
        self._receiver.sendToDevice(self)
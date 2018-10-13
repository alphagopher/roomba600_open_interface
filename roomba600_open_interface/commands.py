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

class StartCommand(Command):
    def __init__(self, receiver):
        self._receiver = receiver
        self.commandName = "StartCommand"
        self.opCode = 128
        self.dataBytes = []

class SafeModeCommand(Command):
    def __init__(self, receiver):
        self._receiver = receiver
        self.commandName = "SafeMode"
        self.opCode = 131
        self.dataBytes = []

class BrushesOnCommand(Command):
    def __init__(self, receiver):
        self._receiver = receiver
        self.commandName = "BrushesOn"
        self.opCode = 144
        self.dataBytes = [100, 100, 100]

class BrushesOffCommand(Command):
    def __init__(self, receiver):
        self._receiver = receiver
        self.commandName = "BrushesOff"
        self.opCode = 144
        self.dataBytes = [0, 0, 0]

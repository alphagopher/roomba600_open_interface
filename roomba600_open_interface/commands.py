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
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "StartCommand"
        self.opCode = 128
        self.dataBytes = dataBytes

class StopCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "StopCommand"
        self.opCode = 173
        self.dataBytes = dataBytes

class SafeModeCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "SafeMode"
        self.opCode = 131
        self.dataBytes = dataBytes

class PwmMotorCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "BrushesOn"
        self.opCode = 144
        self.dataBytes = dataBytes
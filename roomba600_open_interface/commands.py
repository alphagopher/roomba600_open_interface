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

# Command: Start--Opcode 128--Databytes: 0
class StartCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "StartCommand"
        self.opCode = 128
        self.dataBytes = dataBytes

# Command: Reset--Opcode 7--Databytes: 0
class ResetCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "ResetCommand"
        self.opCode = 7
        self.dataBytes = dataBytes

# Command: Stop--Opcode 173--Databytes: 0
class StopCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "StopCommand"
        self.opCode = 173
        self.dataBytes = dataBytes

# Command: Baud--Opcode 129--Databytes: 0
class BaudCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "BaudCommand"
        self.opCode = 129
        self.dataBytes = dataBytes

# Command: Safe--Opcode 131--Databytes: 0
class SafeCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "SafeCommand"
        self.opCode = 131
        self.dataBytes = dataBytes

# Command: Full--Opcode 132--Databytes: 0
class FullCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "FullCommand"
        self.opCode = 132
        self.dataBytes = dataBytes

class PwmMotorCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "PwmMotorCommand"
        self.opCode = 144
        self.dataBytes = dataBytes

class DriveCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "DriveCommand"
        self.opCode = 137
        self.dataBytes = dataBytes

from .command import Command

# Command: Start
# Opcode: 128
class StartCommand(Command):
    def __init__(self, receiver, dataBytes=[], sensorPackets=[]):
        self._receiver = receiver
        self.commandName = "StartCommand"
        self.opCode = 128
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 0
        self.sensorPackets = []
        self.sensorPacketsRequiredLength = 0

# Command: Reset
# Opcode: 7
class ResetCommand(Command):
    def __init__(self, receiver, dataBytes=[], sensorPackets=[]):
        self._receiver = receiver
        self.commandName = "ResetCommand"
        self.opCode = 7
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 0
        self.sensorPackets = []
        self.sensorPacketsRequiredLength = 0

# Command: Stop
# Opcode: 173
class StopCommand(Command):
    def __init__(self, receiver, dataBytes=[], sensorPackets=[]):
        self._receiver = receiver
        self.commandName = "StopCommand"
        self.opCode = 173
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 0
        self.sensorPackets = []
        self.sensorPacketsRequiredLength = 0
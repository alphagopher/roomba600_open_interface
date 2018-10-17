from .command import Command

# Command: Start
# Opcode: 128
# Databytes: 0
class StartCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "StartCommand"
        self.opCode = 128
        self.dataBytes = dataBytes

# Command: Reset
# Opcode: 7
# Databytes: 0
class ResetCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "ResetCommand"
        self.opCode = 7
        self.dataBytes = dataBytes

# Command: Stop
# Opcode: 173
# Databytes: 0
class StopCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "StopCommand"
        self.opCode = 173
        self.dataBytes = dataBytes

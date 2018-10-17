from .command import Command

# Command: Baud
# Opcode: 129
# Databytes: 1
class BaudCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "BaudCommand"
        self.opCode = 129
        self.dataBytes = dataBytes

# Command: Safe
# Opcode: 131
# Databytes: 0
class SafeCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "SafeCommand"
        self.opCode = 131
        self.dataBytes = dataBytes

# Command: Full
# Opcode: 132
# Databytes: 0
class FullCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "FullCommand"
        self.opCode = 132
        self.dataBytes = dataBytes
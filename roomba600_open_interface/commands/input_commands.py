from .command import Command

# Command: Sensors
# Opcode: 142
class SensorsCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "SensorsCommand"
        self.opCode = 142
        self.dataBytes = dataBytes

# Command: QueryList
# Opcode: 149
class QueryListCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "QueryListCommand"
        self.opCode = 149
        self.dataBytes = dataBytes

# Command: Stream
# Opcode: 148
class StreamCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "StreamCommand"
        self.opCode = 148
        self.dataBytes = dataBytes

# Command: Stream
# Opcode: 150
class PauseResumeCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "PauseResumeCommand"
        self.opCode = 150
        self.dataBytes = dataBytes
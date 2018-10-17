from .command import Command

# Command: Sensors
# Opcode: 142
class SensorsCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "SensorsCommand"
        self.opCode = 142
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 1

# Command: QueryList
# Opcode: 149
# TODO fix variable length of dataBytes (N+1)
class QueryListCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "QueryListCommand"
        self.opCode = 149
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 1

# Command: Stream
# Opcode: 148
# TODO fix variable length of dataBytes (N+1)
class StreamCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "StreamCommand"
        self.opCode = 148
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 1


# Command: PauseResume
# Opcode: 150
class PauseResumeCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "PauseResumeCommand"
        self.opCode = 150
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 1

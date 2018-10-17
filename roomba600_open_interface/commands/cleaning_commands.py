from .command import Command

# Command: Clean
# Opcode: 135
class CleanCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "CleanCommand"
        self.opCode = 135
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 0

# Command: Max
# Opcode: 136
class MaxCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "MaxCommand"
        self.opCode = 136
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 0

# Command: Spot
# Opcode: 134
class SpotCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "SpotCommand"
        self.opCode = 134
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 0

# Command: SeekDock
# Opcode: 143
class SeekDockCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "SeekDockCommand"
        self.opCode = 143
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 0

# Command: Power
# Opcode: 133
class PowerCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "PowerCommand"
        self.opCode = 133
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 0

# Command: Schedule
# Opcode: 167
class ScheduleCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "ScheduleCommand"
        self.opCode = 167
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 15

# Command: SetDayTime
# Opcode: 168
class SetDayTimeCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "SetDayTimeCommand"
        self.opCode = 168
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 3
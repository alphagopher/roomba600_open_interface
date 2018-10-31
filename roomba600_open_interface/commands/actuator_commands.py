from .command import Command

# Command: Drive
# Opcode: 137
class DriveCommand(Command):
    def __init__(self, receiver, dataBytes=[], sensorPackets=[]):
        self._receiver = receiver
        self.commandName = "DriveCommand"
        self.opCode = 137
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 4
        self.sensorPackets = []
        self.sensorPacketsRequiredLength = 0

# Command: DriveDirect
# Opcode: 145
class DriveDirectCommand(Command):
    def __init__(self, receiver, dataBytes=[], sensorPackets=[]):
        self._receiver = receiver
        self.commandName = "DriveDirectCommand"
        self.opCode = 145
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 4
        self.sensorPackets = []
        self.sensorPacketsRequiredLength = 0

# Command: DrivePwm
# Opcode: 146
class DrivePwmCommand(Command):
    def __init__(self, receiver, dataBytes=[], sensorPackets=[]):
        self._receiver = receiver
        self.commandName = "DrivePwmCommand"
        self.opCode = 146
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 4
        self.sensorPackets = []
        self.sensorPacketsRequiredLength = 0

# Command: Motors
# Opcode: 138
# Databytes: 1
class MotorsCommand(Command):
    def __init__(self, receiver, dataBytes=[], sensorPackets=[]):
        self._receiver = receiver
        self.commandName = "MotorsCommand"
        self.opCode = 138
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 1
        self.sensorPackets = []
        self.sensorPacketsRequiredLength = 0       

# Command: PwmMotors
# Opcode: 144
# Databytes: 3
class PwmMotorsCommand(Command):
    def __init__(self, receiver, dataBytes=[], sensorPackets=[]):
        self._receiver = receiver
        self.commandName = "PwmMotorsCommand"
        self.opCode = 144
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 3
        self.sensorPackets = []
        self.sensorPacketsRequiredLength = 0

# Command: LEDs
# Opcode: 139
# Databytes: 3
class LEDsCommand(Command):
    def __init__(self, receiver, dataBytes=[], sensorPackets=[]):
        self._receiver = receiver
        self.commandName = "LEDsCommand"
        self.opCode = 139
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 3

# Command: SchedulingLEDs
# Opcode: 162
# Databytes: 2
class SchedulingLEDsCommand(Command):
    def __init__(self, receiver, dataBytes=[], sensorPackets=[]):
        self._receiver = receiver
        self.commandName = "SchedulingLEDsCommand"
        self.opCode = 162
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 2
        self.sensorPackets = []
        self.sensorPacketsRequiredLength = 0

# Command: DigitLEDsRaw
# Opcode: 163
class DigitLEDsRawCommand(Command):
    def __init__(self, receiver, dataBytes=[], sensorPackets=[]):
        self._receiver = receiver
        self.commandName = "DigitLEDsRawCommand"
        self.opCode = 163
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 4
        self.sensorPackets = []
        self.sensorPacketsRequiredLength = 0

# Command: Buttons
# Opcode: 165
class ButtonsCommand(Command):
    def __init__(self, receiver, dataBytes=[], sensorPackets=[]):
        self._receiver = receiver
        self.commandName = "ButtonsCommand"
        self.opCode = 165
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 1
        self.sensorPackets = []
        self.sensorPacketsRequiredLength = 0

# Command: DigitLEDsAscii
# Opcode: 164
class DigitLEDsAsciiCommand(Command):
    def __init__(self, receiver, dataBytes=[], sensorPackets=[]):
        self._receiver = receiver
        self.commandName = "DigitLEDsAsciiCommand"
        self.opCode = 164
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 4
        self.sensorPackets = []
        self.sensorPacketsRequiredLength = 0

# Command: Song
# Opcode: 140
# TODO: Improve validation to be 2N+2 length where n is number of notes in song
class SongCommand(Command):
    def __init__(self, receiver, dataBytes=[], sensorPackets=[]):
        self._receiver = receiver
        self.commandName = "SongCommand"
        self.opCode = 140
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 4
        self.sensorPackets = []
        self.sensorPacketsRequiredLength = 0

# Command: Play
# Opcode: 141
class PlayCommand(Command):
    def __init__(self, receiver, dataBytes=[], sensorPackets=[]):
        self._receiver = receiver
        self.commandName = "PlayCommand"
        self.opCode = 141
        self.dataBytes = dataBytes
        self.dataBytesRequiredLength = 1
        self.sensorPackets = []
        self.sensorPacketsRequiredLength = 0        
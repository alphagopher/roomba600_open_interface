from .command import Command

# Command: Drive
# Opcode: 137
# Databytes: 4
class DriveCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "DriveCommand"
        self.opCode = 137
        self.dataBytes = dataBytes

# Command: DriveDirect
# Opcode: 145
# Databytes: 4
class DriveDirectCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "DriveDirectCommand"
        self.opCode = 145
        self.dataBytes = dataBytes

# Command: DrivePwm
# Opcode: 146
# Databytes: 4
class DrivePwmCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "DrivePwmCommand"
        self.opCode = 146
        self.dataBytes = dataBytes

# Command: Motors
# Opcode: 138
# Databytes: 1
class MotorsCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "MotorsCommand"
        self.opCode = 138
        self.dataBytes = dataBytes        

# Command: PwmMotors
# Opcode: 144
# Databytes: 3
class PwmMotorsCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "PwmMotorsCommand"
        self.opCode = 144
        self.dataBytes = dataBytes

# Command: LEDs
# Opcode: 139
# Databytes: 3
class LEDsCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "LEDsCommand"
        self.opCode = 139
        self.dataBytes = dataBytes

# Command: SchedulingLEDs
# Opcode: 162
# Databytes: 2
class SchedulingLEDsCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "SchedulingLEDsCommand"
        self.opCode = 162
        self.dataBytes = dataBytes

# Command: DigitLEDsRaw
# Opcode: 163
class DigitLEDsRawCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "DigitLEDsRawCommand"
        self.opCode = 163
        self.dataBytes = dataBytes

# Command: Buttons
# Opcode: 165
class ButtonsCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "ButtonsCommand"
        self.opCode = 165
        self.dataBytes = dataBytes

# Command: DigitLEDsAscii
# Opcode: 164
class DigitLEDsAsciiCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "DigitLEDsAsciiCommand"
        self.opCode = 164
        self.dataBytes = dataBytes

# Command: Song
# Opcode: 140
class SongCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "SongCommand"
        self.opCode = 140
        self.dataBytes = dataBytes

# Command: Play
# Opcode: 141
class PlayCommand(Command):
    def __init__(self, receiver, dataBytes=[]):
        self._receiver = receiver
        self.commandName = "PlayCommand"
        self.opCode = 141
        self.dataBytes = dataBytes
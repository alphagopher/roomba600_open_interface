class Command:
    def __init__(self, commandName, opCode, dataBytes=[]):
        self.commandName = commandName
        self.opCode = opCode
        self.dataBytes = dataBytes
        
    def getByteArray(self):
        return bytes([self.opCode] + self.dataBytes)

class StartCommand(Command):
    def __init__(self):
        Command.__init__(self, "START", 128, [])
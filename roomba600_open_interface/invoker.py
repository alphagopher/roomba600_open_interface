from roomba600_open_interface.commands.command import Command

class Invoker:
    """
    Ask the command to carry out the request.
    TODO: Consider "Composite" pattern for command structures
    """

    def __init__(self):
        self._commands = []
        self._Debug = False

    def storeCommand(self, command):
        if(command.isValid()):
            self._commands.append(command)
            if(self._Debug == True):
                print("Stored Command - ", command.toLogString())
        else:
            print("Could Not Store Invalid Command - ", command.toLogString())

    def executeCommands(self):
        if(self._Debug == True):
            print("-----Executing ", len(self._commands), "Commands-----")

        for command in self._commands:
            command.execute()
        self._commands = []

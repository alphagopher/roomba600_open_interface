class Invoker:
    """
    Ask the command to carry out the request.
    """

    def __init__(self):
        self._commands = []

    def storeCommand(self, command):
        self._commands.append(command)

    def executeCommands(self):
        for command in self._commands:
            command.execute()

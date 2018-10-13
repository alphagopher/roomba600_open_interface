from open_interface.receivers import SerialReceiver
from open_interface.commands import *
from open_interface.invoker import Invoker

import time

# receiver = Receiver()
# concrete_command = ConcreteCommand(receiver)

receiver = SerialReceiver("COM3")

invoker = Invoker()

invoker.storeCommand(StartCommand(receiver))
invoker.storeCommand(SafeModeCommand(receiver))
invoker.executeCommands()

time.sleep(.6)

invoker.storeCommand(BrushesOnCommand(receiver))
invoker.executeCommands()
time.sleep(.6)
invoker.storeCommand(BrushesOffCommand(receiver))
invoker.executeCommands()

# invoker = Invoker()
# invoker.store_command(concrete_command)
# invoker.execute_commands()

# startCommand = StartCommand()

# robotReceiver = SerialConnection('COM3')

# robotReceiver.sendCommand(START)

# robotReceiver.moveForward()
# robotReceiver.moveBackward()
# robotReceiver.turnLeft()
# robotReceiver.turnRight()
# robotReceiver.brushesOn()
# time.sleep(.6)
# robotReceiver.brushesOff()
# robotReceiver.shutDown()
# #done!
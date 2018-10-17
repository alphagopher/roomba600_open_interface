from roomba600_open_interface.receivers import SerialReceiver
from roomba600_open_interface.commands.getting_started_commands import StartCommand, StopCommand
from roomba600_open_interface.commands.mode_commands import SafeCommand
from roomba600_open_interface.commands.actuator_commands import PwmMotorsCommand
from roomba600_open_interface.invoker import Invoker

import time

receiver = SerialReceiver("COM3")

invoker = Invoker()

invoker.storeCommand(StartCommand(receiver))
invoker.storeCommand(SafeCommand(receiver))
invoker.executeCommands()

time.sleep(.6)

# start brushes
invoker.storeCommand(PwmMotorsCommand(receiver, [100, 100, 100]))
invoker.executeCommands()

time.sleep(.6)
# stop brushes
invoker.storeCommand(PwmMotorsCommand(receiver, [0, 0, 0]))
invoker.storeCommand(StopCommand(receiver))
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
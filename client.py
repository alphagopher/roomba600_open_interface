from roomba600_open_interface.receivers import RoombaSerialConnection
from roomba600_open_interface.commands.getting_started_commands import StartCommand, StopCommand
from roomba600_open_interface.commands.mode_commands import SafeCommand
from roomba600_open_interface.commands.actuator_commands import PwmMotorsCommand
from roomba600_open_interface.invoker import Invoker

import time

roombaConnection = RoombaSerialConnection("COM3")

invoker = Invoker()

invoker.storeCommand(StartCommand(roombaConnection))
invoker.storeCommand(SafeCommand(roombaConnection))
invoker.executeCommands()

time.sleep(.6)

# start brushes
invoker.storeCommand(PwmMotorsCommand(roombaConnection, [100, 100, 100]))
invoker.executeCommands()

time.sleep(.6)
# stop brushes
invoker.storeCommand(PwmMotorsCommand(roombaConnection, [0, 0, 0]))
invoker.storeCommand(StopCommand(roombaConnection))
invoker.executeCommands()
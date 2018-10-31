from roomba600_open_interface.receivers import RoombaSerialConnection
from roomba600_open_interface.commands.getting_started_commands import StartCommand, StopCommand
from roomba600_open_interface.commands.mode_commands import SafeCommand, FullCommand
from roomba600_open_interface.commands.actuator_commands import PwmMotorsCommand
from roomba600_open_interface.commands.input_commands import SensorsCommand
from roomba600_open_interface.invoker import Invoker
from roomba600_open_interface.packets.packets import ChargingStateSensorPacket, BatteryChargeSensorPacket, BatteryCapacitySensorPacket
from roomba600_open_interface.packets.packets import OpenInterfaceModeSensorPacket

import time

roombaConnection = RoombaSerialConnection("COM3")

invoker = Invoker()

invoker.storeCommand(StartCommand(roombaConnection))
invoker.executeCommands()

time.sleep(1)

invoker.storeCommand(SensorsCommand(receiver=roombaConnection, dataBytes=[], sensorPackets=[BatteryChargeSensorPacket()]))
invoker.executeCommands()

time.sleep(1)

invoker.storeCommand(SafeCommand(roombaConnection))
invoker.executeCommands()

time.sleep(1)

invoker.storeCommand(SensorsCommand(receiver=roombaConnection, dataBytes=[], sensorPackets=[OpenInterfaceModeSensorPacket()]))
invoker.executeCommands()

time.sleep(.5)

invoker.storeCommand(FullCommand(roombaConnection))
invoker.executeCommands()

time.sleep(.5)

invoker.storeCommand(SensorsCommand(receiver=roombaConnection, dataBytes=[], sensorPackets=[OpenInterfaceModeSensorPacket()]))
invoker.executeCommands()

time.sleep(1)

time.sleep(.3)

invoker.storeCommand(SensorsCommand(receiver=roombaConnection, dataBytes=[], sensorPackets=[ChargingStateSensorPacket()]))
invoker.executeCommands()

time.sleep(.3)

# start brushes
invoker.storeCommand(PwmMotorsCommand(roombaConnection, [100, 100, 100]))
invoker.executeCommands()

time.sleep(.3)

invoker.storeCommand(SensorsCommand(receiver=roombaConnection, dataBytes=[], sensorPackets=[ChargingStateSensorPacket()]))
invoker.executeCommands()

time.sleep(.6)
# stop brushes
invoker.storeCommand(PwmMotorsCommand(roombaConnection, [0, 0, 0]))
invoker.executeCommands()

time.sleep(.6)

invoker.storeCommand(SensorsCommand(receiver=roombaConnection, dataBytes=[], sensorPackets=[BatteryCapacitySensorPacket()]))
invoker.executeCommands()

time.sleep(.6)

invoker.storeCommand(StopCommand(roombaConnection))
invoker.executeCommands()

roombaConnection.close()
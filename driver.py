from open_interface.serial_connection import SerialConnection
import time
robot = SerialConnection('COM3')

robot.moveForward()
robot.moveBackward()
robot.turnLeft()
robot.turnRight()
robot.brushesOn()
time.sleep(.6)
robot.brushesOff()
robot.shutDown()
#done!
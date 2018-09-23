import roomba_interface
import time
robot = roomba_interface.SerialConnection('COM3')

robot.moveForward()
robot.moveBackward()
robot.turnLeft()
robot.turnRight()
robot.shutDown()
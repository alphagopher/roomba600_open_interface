import open_interface
import time
robot = open_interface.SerialConnection('COM3')

robot.moveForward()
robot.moveBackward()
robot.turnLeft()
robot.turnRight()
robot.brushesOn()
time.sleep(.6)
robot.brushesOff()
robot.shutDown()
#done!
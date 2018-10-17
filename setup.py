from setuptools import setup

setup(
   name='roomba600_open_interface',
   version='0.1.0',
   description='A python implementation of the iRobot Create2 / Roomba 600 Series Serial Open Interface Specification.',
   author='Andrew Porter',
   author_email='porter.andrewsteven@gmail.com',
   license='MIT',
   packages=['roomba600_open_interface'],
   install_requires=['pyserial==3.4']
)
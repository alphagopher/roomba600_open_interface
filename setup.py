from setuptools import setup

setup(
   name='roomba600_open_interface',
   version='1.0',
   description='An implementation of the Roomba 600 / Create 2 Open Interface Specification so you can control your Roomba with Python!',
   author='Andre Porter',
   author_email='porter.andrewsteven@gmail.com',
   packages=['roomba600_open_interface'],  #same as name
   install_requires=['pyserial', 'greek'], #external packages as dependencies
)
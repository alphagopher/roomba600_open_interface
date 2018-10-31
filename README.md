# Background
Roombas manufactured after October 2008 have a Serial Port that is a female DIN connector. This serial interface can be used to control and receive information from the Roomba using something like a Raspberry Pi, Arduino, or general laptop computer. iRobot published the Open Interface Specification for how to communicate with Roomba. This repository is an implementation of the iRobot Roomba Create2 / Roomba 600 Series Open Interface.

The intent of this interface implementation is a pet project to enable others a re-usable library to experiment with their Roombas.

# Architecture
* Command / Receiver / Invoker / Client behavioral design pattern

# Project Setup
* Runs on Rasperry Pi connected to Roomba 671 via Serial Port
* Set of endpoints that forward requests to Roomba Driver

# References
* Abstraction layer for [iRobot Roomba Create 2 / 600 Series Open Interface Spec](https://www.irobotweb.com/~/media/MainSite/PDFs/About/STEM/Create/iRobot_Roomba_600_Open_Interface_Spec.pdf)
* [USB to DIN Cable For Connecting to Roomba Serial Port](https://www.amazon.com/EZSync-Serial-Roomba-Create-EZSync018/dp/B06XDPMY4Z)

# Sample Raw pyserial Code
```python
import serial
# Open new connection (NOTE, change port)
ser = serial.Serial("COM3", baudrate=115200, timeout=0.5)
# Send "Start" Opcode to start Open Interface, Roomba in Passive Mode
ser.write(bytes([128]))
# Send "Safe Mode" Opcode to enable Roomba to respond to commands
ser.write(bytes([131]))
# Start Brushes
ser.write(bytes([144,100,100,100]))
timer.sleep(.6)
# Stop Brushes
ser.write(bytes([144,0,0,0]))
```

# TODO
* Add validators to commands for data bytes
* Add remaining commands
* Add Logging




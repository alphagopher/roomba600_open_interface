# roomba_interface
Code to run on Raspberry Pi connected to Roomba via serial port

This is a part of a project to build a mobile application remote control for my Roomba. The general architecture is as follows

# Roomba Client Controller
* User Interface / Remote Control for Roomba 671
* Sends requests to Roomba Server

# Roomba Server
* Runs on Rasperry Pi connected to Roomba 671 via Serial Port
* Set of endpoints that forward requests to Roomba Driver

# Roomba Driver / Interface
* Runs on Rasperry Pi connected to Roomba 671 via Serial Port
* Abstraction layer for [iRobot Roomba Create 2 / 600 Series Open Interface Spec](https://www.irobotweb.com/~/media/MainSite/PDFs/About/STEM/Create/iRobot_Roomba_600_Open_Interface_Spec.pdf)
* Low-level components that wrap Roomba Open Interface commands (byte arrays)
* Provides useable roomba command interface (move forward, turn, brushes on / off)

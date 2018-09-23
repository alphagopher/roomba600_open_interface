# roomba_interface
Code to run on Raspberry Pi connected to Roomba via serial port

This is a part of a project to build a mobile application remote control for my Roomba. The general architecture is as follows

Roomba Client Controller
  User Interface / Remote Control for Roomba

Roomba Server
  Runs on Rasperry Pi connected to Roomba 671 via Serial Port
  Set of endpoints that forward requests to Roomba Driver

Roomba Driver / Interface
  Runs on Rasperry Pi connected to Roomba 671 via Serial Port
  Low-level components that wrap Roomba Open Interface commands (byte arrays)
  Provides useable roomba command interface (move forward, turn, brushes on / off)

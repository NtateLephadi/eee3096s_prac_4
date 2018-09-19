#!/usr/bin/python

import spidev
import time
from gpiozero import MCP3008, Button

MCP3008(channel=0)

potentiometer=MCP3008(0)
light_sensor=MCP3008(1)
temperature_sensor=MCP3008(2)

current_voltage=potentiometer.voltage
current_light=light_sensor.value * 100
current_temperature=yield(temperature_sensor.value * 3.3 - 0.5) * 100

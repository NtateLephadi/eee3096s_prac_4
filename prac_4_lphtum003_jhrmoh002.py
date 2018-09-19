#!/usr/bin/python

import spidev
import time
from gpiozero import MCP3008, Button, LightSensor

MCP3008(channel=0, differential=False, max_voltage=3.3, clock_pin=11, mosi_pin=10, miso_pin=9, select_pin=8)

potentiometer=MCP3008(0)
print(potentiometer.values)

temperature_sensor=MCP3008(2)
print(temperature_sensor.value)

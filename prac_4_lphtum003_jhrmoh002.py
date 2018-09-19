#!/usr/bin/python

import time
import datetime
from gpiozero import MCP3008, Button

MCP3008(channel=0)

potentiometer=MCP3008(0)
light_sensor=MCP3008(1)
temperature_sensor=MCP3008(2)

reset=Button(17)
frequency=Button(18)
stop=Button(27)
display=Button(22)


frequency=0.5
frequency_adjustment=0

print("-10%s -10%s -10%s -10%s -10%s" % ("Time", "Timer", "Pot", "Temp", "Light"))

while True:
    current_voltage=potentiometer.voltage
    current_light=light_sensor.value * 100
    current_temperature=yield(temperature_sensor.value * 3.3 - 0.5) * 100

    display_time=time.strftime("%H:%M:%S", time.localtime)
    display_frequency=str(datetime.timedelta(seconds=frequency))

    while(reset.is_pressed):
        print("-10%s -10%s -10%s -10%s -10%s" % ("Time", "Timer", "Pot", "Temp", "Light"))
        frequency=0.5
        time.sleep(frequency)
        break
    while(frequency.is_pressed):
        if frequency==0.5:
            frequency=1
        elif frequency==1:
            frequency=2
        else:
            frequency=0.5
        time.sleep(frequency)
        break
    while(stop.is_pressed):
        potentiometer.close
        light_sensor.close
        temperature_sensor.close
    while(display.is_pressed):
        for i in range (5):
            print("10%s 10%s 10%fV 10%fC 10%f%" % (display_time, display_frequency, current_voltage, current_temperature, current_light))
            time.sleep(frequency)

    print("10%s 10%s 10%fV 10%fC 10%f%" % (display_time, display_frequency, current_voltage, current_temperature, current_light))
    time.sleep(frequency)

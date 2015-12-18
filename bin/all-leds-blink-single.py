#!/usr/bin/python
pos="/home/pi/gpio-glyphs/bin/"
import RPi.GPIO as gpio
import json
import time
flag=False
gpio.setwarnings(False)
delay=1
gpio.setmode(gpio.BOARD)
conv=json.load(open(pos+"conv.json"))
for i in conv:
	gpio.setup(conv[i],gpio.OUT)
for j in range(0,2):
	flag=not flag
	for i in conv:gpio.output(conv[i],flag)
	time.sleep(delay)

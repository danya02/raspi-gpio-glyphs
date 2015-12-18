#!/usr/bin/python
pos="/home/pi/gpio-glyphs/bin/"
import RPi.GPIO as gpio
import time
import json
gpio.setwarnings(False)
delay=0.5
conv=json.load(open(pos+"conv.json"))
list=[conv["1"],conv["2"],conv["3"],conv["4"],conv["5"],conv["6"],conv["7"],conv["8"],conv["9"],conv["10"],conv["11"]]
gpio.setmode(gpio.BOARD)
gpio.setup(list,gpio.OUT)
for i in list:
	gpio.output(i,0)
	time.sleep(delay)

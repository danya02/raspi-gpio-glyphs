pos="/home/pi/gpio-glyphs/bin/"
import RPi.GPIO as gpio
import json
import time
flag=True
gpio.setwarnings(False)
delay=0.05
gpio.setmode(gpio.BOARD)
conv=json.load(open(pos+"conv.json"))
for i in conv:
	gpio.setup(conv[i],gpio.OUT)
while 1:
	flag=not flag
	for i in conv:gpio.output(conv[i],flag)
	time.sleep(delay)

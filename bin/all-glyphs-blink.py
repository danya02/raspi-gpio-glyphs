pos="/home/pi/gpio-glyphs/bin/"
import json
import time
import RPi.GPIO as gpio
gpio.setwarnings(False)
dict=json.load(open(pos+"dict.json"))
iter=0
conv=json.load(open(pos+"conv.json"))
gpio.setmode(gpio.BOARD)
conv=[conv["1"],conv["2"],conv["3"],conv["4"],conv["5"],conv["6"],conv["7"],conv["8"],conv["9"],conv["10"],conv["11"]]
while 1:
	time.sleep(0.1)
	iter=iter+1
	if iter>len(dict["leds"]):iter=0
	for i in conv:
		gpio.setup(i,gpio.OUT)
		gpio.output(i,0)
	for i in dict["leds"][iter-1]:
		gpio.setup(conv[i-1],gpio.OUT)
		gpio.output(conv[i-1],1)

import json
import time
import RPi.GPIO as gpio
gpio.setwarnings(False)
dict=json.load(open("dict.json"))
iter=0
gpio.setmode(gpio.BOARD)
conv=[33,5,19,10,18,40,13,15,3,26,11]
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

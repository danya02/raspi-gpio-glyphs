import json
import RPi.GPIO as gpio
gpio.setwarnings(False)
dict=json.load(open("dict.json"))
iter=0
gpio.setmode(gpio.BOARD)
conv=[33,5,19,10,18,40,13,15,3,26,11]
print("Choose which Shaper glyph you would like to display:")
for i in dict["def"]:
	iter=iter+1
	print(str(iter)+". "+i)
disp=int(raw_input("choice> "))
for i in conv:
        gpio.setup(i,gpio.OUT)
        gpio.output(i,0)
for i in dict["leds"][disp-1]:
	gpio.setup(conv[i-1],gpio.OUT)
	gpio.output(conv[i-1],1)

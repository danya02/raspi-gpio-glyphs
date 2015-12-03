import json
import RPi.GPIO as gpio
gpio.setwarnings(False)
dict=json.load(open("dict.json"))
iter=0
gpio.setmode(gpio.BOARD)
conv=json.loads(open("conv.json").read())
conv_orig=[conv["1"],conv["2"],conv["3"],conv["4"],conv["5"],conv["6"],conv["7"],conv["8"],conv["9"],conv["10"],conv["11"]]
print("Choose which Shaper glyph you would like to display:")
for i in dict["def"]:
	iter=iter+1
	print(str(iter)+". "+i)
disp=int(raw_input("choice> "))
gpio.setup(conv_orig,gpio.OUT)
gpio.output(conv_orig,0)
for i in dict["leds"][disp-1]:
	gpio.setup(conv[str(i)],gpio.OUT)
	gpio.output(conv[str(i)],1)

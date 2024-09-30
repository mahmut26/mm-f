import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)

while True:
	ifGPIO.input(23)==1:
		whileGPIO.input(23)==0:
			os.system("sudorebootnow")

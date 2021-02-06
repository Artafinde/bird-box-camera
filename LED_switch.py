import RPi.GPIO as gpio

led_pin = 18

led_logic = int(input('\nEnter 1 to turn pin '+str(led_pin)+' on, or 0 to turn off\n'))

if led_logic not in [1,0]:
	print('\nLED SETTING MUST BE 1 OR 0!\n')
else:
	gpio.setmode(gpio.BCM)
	gpio.setup(led_pin, gpio.OUT)
	if led_logic==1:
		print('\nSwitching on pin '+str(led_pin)+'\n')
	else:
		print('\nSwitching off pin '+str(led_pin)+'\n')
	gpio.output(led_pin,led_logic)



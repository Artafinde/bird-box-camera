import RPi.GPIO as gpio
import time
import subprocess
import sys, os, signal

#Setup LED pin and initialise to off
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
led_pin = 18
gpio.setup(led_pin, gpio.OUT)
gpio.output(led_pin,0)

#Turn camera on. Direct output to /dev/null
print("Turning camera on...")
cam_proc = subprocess.Popen(['python3','camera_streamer.py'],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

#Output URL info to terminal
ip = str( subprocess.run(["hostname","-I"],capture_output=True).stdout )
ip = ip[ ip.find('\'')+1 : ip.rfind(' ')]
print("\nCamera streaming to URL: http://" + ip + ":8000/")

#Ask if want to turn LED on
ans = input('\nTurn LEDs on? (y/n)')
if ans == 'y':
    print('\nLEDs turning on')
    gpio.output(led_pin,1)
else:
    print('\nLEDs remaining off')
    
#Wait for input then turn LED and camera off
input("\nKeystroke to turn off camera")
gpio.output(led_pin,0)
cam_proc.terminate()


input("\nKeystroke to exit")





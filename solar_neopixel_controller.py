from datetime import datetime
from astral import Observer
from astral.sun import sun
import board
import neopixel

# Time (seconds) after sunrise and before sunset to switch neopixels
neopixel_lag =  30*60 #half an hour seems reasonable

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 8

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

#Create pixels object
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.02, auto_write=False, pixel_order=ORDER
)

#Create sun object for Oxford today
longitude = -1.2577
lattitude = 51.7520
s=sun(Observer(lattitude,longitude), date=datetime.today(), dawn_dusk_depression=6.0)

#Print sun times for info
print((
    f'Dawn:    {s["dawn"]}\n'
    f'Sunrise: {s["sunrise"]}\n'
    f'Noon:    {s["noon"]}\n'
    f'Sunset:  {s["sunset"]}\n'
    f'Dusk:    {s["dusk"]}\n'
))

#Obtain sun times as UNIX timestamps
dawn = s["dawn"].timestamp()
sunrise = s["sunrise"].timestamp()
sunset = s["sunset"].timestamp()
dusk = s["dusk"].timestamp()

#Get current time as UNIX timestamp, to compare to today's solar cycle
time_now = datetime.now().timestamp()

#Compare current time to today's solar cycle, and act accordingly
if time_now<(sunrise+neopixel_lag) or time_now>=(sunset-neopixel_lag):
    #Nighttime, so set all colours to zero
    r=0
    g=0
    b=0
    print("it is night")
    
elif time_now>=sunrise and time_now<sunset:
    #Daytime, so set all colurs to maximum
    r=255
    g=255
    b=255
    print("it is day")

#Set neopixel colours
pixels[0] = (r,g,b)
pixels[7] = (r,g,b)
for i in range(1,7):
    pixels[i] = (0,0,0)
pixels.show()
exit()


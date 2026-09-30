from machine import Pin
import utime

LEDPIN = 16
BUTTPIN = 18

LED = Pin(LEDPIN, Pin.OUT)
BUTTON = Pin(BUTTPIN, Pin.IN)

ledstate = False

f = 500000000 #ns
lastChangeTime = 0
currTime = 0

while True:
    currTime = utime.time_ns()
    
    if (currTime - lastChangeTime) >= f:
        ledstate = not(ledstate)
        lastChangeTime = currTime
    
    LED.value(ledstate)
    
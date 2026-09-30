from machine import Pin

LEDPIN = 16
BUTTPIN = 18

LED = Pin(LEDPIN, Pin.OUT)
BUTTON = Pin(BUTTPIN, Pin.IN)

while(1):
    LED.value(BUTTON.value())

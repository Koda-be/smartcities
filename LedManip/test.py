from machine import Pin
import utime

try:
    LEDPIN = 16
    BUTTPIN = 18

    notPressed = 0
    pressed = 1
    longPressed = 2

    LONGPRESSTIME = 500000000 #ns

    LED = Pin(LEDPIN, Pin.OUT)
    BUTTON = Pin(BUTTPIN, Pin.IN)

    pressType = notPressed
    periodChanged = False
    ledstate = False

    defaultPeriod = 500000000 # ns
    period = defaultPeriod
    lastChangeTime = 0
    lastPress = 0
    lastPressTime = 0

    currTime = 0

    while True:
        currTime = utime.time_ns()
        
        if BUTTON.value():
            if pressType == notPressed:
                lastPressTime = currTime
                pressType = pressed
                print("pressed")

            elif (currTime - lastPressTime) >= LONGPRESSTIME:
                lastPressTime = currTime
                pressType = longPressed
                print("long pressed")
            
        else: 
            if (pressType == pressed) or (pressType == longPressed): print("released")
            pressType = notPressed
            periodChanged = False


        if (pressType == pressed) and (not periodChanged):
            period /= 2
            print(f"new freq: {period}")
            periodChanged = True

        elif pressType == longPressed:
            period = defaultPeriod

        if (currTime - lastChangeTime) >= period:
            ledstate = not(ledstate)
            lastChangeTime = currTime
        
        LED.value(ledstate)

except KeyboardInterrupt:
    print("Program stopped")
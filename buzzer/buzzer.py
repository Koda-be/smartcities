from machine import ADC, Pin
import utime

starttime = utime.time()

def getPWM(rangemin, rangemax, value, maxDuty):
    if value <= rangemin: return 0
    if value >= rangemax: return 100

    m = maxDuty/(rangemax - rangemin)
    p = -rangemin * m
    return (m*value + p)

try:
    rotAngSen = ADC(0)
    led = Pin(16)

    while True:
        val = rotAngSen.read_u16()
        print(f"{val}, {getPWM(336, 65535, val, 1000)}")
        utime.sleep(1)

except KeyboardInterrupt:
    print(f"Program ended after {utime.time() - starttime} seconds")
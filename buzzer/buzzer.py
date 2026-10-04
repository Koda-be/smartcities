from machine import ADC
import utime

starttime = utime.time()

try:
    rotAngSen = ADC(0)

    while True:
        print(rotAngSen.read_u16())
        utime.sleep(1)

except KeyboardInterrupt:
    print(f"Program ended after {utime.time() - starttime} seconds")
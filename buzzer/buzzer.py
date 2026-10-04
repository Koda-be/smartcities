from machine import ADC, Pin, PWM
import utime

starttime = utime.time()

def getPWM(rangemin, rangemax, value, maxDuty):
    if value <= rangemin: return (0)
    if value >= rangemax: return (maxDuty)

    m = maxDuty/(rangemax - rangemin)
    p = -rangemin * m
    return round(m*value + p)

try:

    rotAngSen = ADC(0)
    buzzer = PWM(Pin(27))

    STOP = 0
    DO = 1046
    RE = 1175
    MI = 1318
    FA = 1397
    SOL = 1568
    LA = 1760
    SI = 1967

    song = [[DO, 0.5], [MI, 0.5], [LA, 0.5], [DO*2, 0.3], [STOP, 0.2], [DO*2, 0.5], [LA, 0.5], [MI, 0.5], [DO, 0.3], [STOP, 0.2]]
    N = 0
    D = 1

    i = 0

    lastNoteChange = 0
    
    buzzer.freq(song[0][N])

    while True:
        currTime = utime.time_ns()
        duty = rotAngSen.read_u16()

        if song[i][N] == 0:
            duty = 0

        if(currTime - lastNoteChange) >= song[i][D]*1000000000:
            i = ((i + 1) if i < len(song)-1 else 0)
            print(f"curr note: {song[i][N]}")
            if song[i][N] == 0:
                duty = 0
            else:
                buzzer.freq(song[i][N])

            lastNoteChange = currTime
        
        buzzer.duty_u16(getPWM(336, 65535, duty, 1000))

        


except KeyboardInterrupt:
    print(f"Program ended after {utime.time() - starttime} seconds")
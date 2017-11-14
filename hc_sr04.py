import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.IN)

def checkdistance():
    GPIO.output(3, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(3, GPIO.LOW)
    while(not GPIO.input(5)):
        pass
    start = time.time()
    while(GPIO.input(5)):
        if(time.time() - start > 0.026):
            break
    end = time.time()
    
    return (end - start) * 340 / 2

try:
    while(True):
        print('Distance: %0.2f m' %checkdistance())
        time.sleep(.5)
except KeyboardInterrupt:
    GPIO.cleanup()

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

p = GPIO.PWM(7, 1000)
p.start(0)

try:
    while(True):
        duty_cycle = input('Please input duty cycle:\n')
        p.ChangeDutyCycle(float(duty_cycle))
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()


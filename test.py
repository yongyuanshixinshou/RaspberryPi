import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup((3, 5), GPIO.OUT, initial=GPIO.LOW)



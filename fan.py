#! /usr/bin/python3

import time, os
import RPi.GPIO as GPIO


def get_cpu_temp():
    temp = 0
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        temp = float(f.read()) / 1000.0
    return temp

class Fan:
    def __init__(self, enabel_io, speed=0):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(enabel_io, GPIO.OUT, initial=GPIO.HIGH)
        self.enabel_io = enabel_io
    
    def start(self):
        GPIO.output(self.enabel_io, GPIO.LOW)
    
    def stop(self):
        GPIO.output(self.enabel_io, GPIO.HIGH)
    

if __name__ == '__main__':
    fan = Fan(7)
    try:
        while(True):
            temp = get_cpu_temp()
            if temp <= 40:
                fan.stop()
            if temp >= 45:
                fan.start()
            print('temp: %0.2f' %temp)
            time.sleep(1)
    except KeyboardInterrupt:
        fan.stop()
        GPIO.cleanup()
    

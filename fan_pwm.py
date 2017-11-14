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
        GPIO.setup(enabel_io, GPIO.OUT, initial=GPIO.LOW)
        self.__enabel_pwm = GPIO.PWM(enabel_io, 20)
        self.__speed = speed
    
    def start(self):
        self.__enabel_pwm.start(100)
    
    def stop(self):
        self.__enabel_pwm.stop()
    
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed
        self.__enabel_pwm.ChangeDutyCycle(speed)

if __name__ == '__main__':
    fan = Fan(8)
    fan.start()
    try:
        while(True):
            temp = get_cpu_temp()
            speed = (temp - 40) * 10
            if speed <= 0:
                speed = 0
            if speed >= 100:
                speed = 100
            fan.speed = 100 - speed
            print('temp: %0.2f' %temp)
            print('speed: %0.2f' %fan.speed)
            print('--------------------------------')
            time.sleep(1)
    except KeyboardInterrupt:
        fan.stop()
        GPIO.cleanup()
    

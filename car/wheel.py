import RPi.GPIO as GPIO

class Wheel:
    def __init__(self, in1, in2, enable, pwm=False):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup((in1, in2, enable), GPIO.OUT, initial=GPIO.LOW)
        GPIO.setwarnings(False)
        self.__in1 = in1
        self.__in2 = in2
        self.__pwm = pwm
        if not self.__pwm:
            GPIO.output(enable, GPIO.HIGH)
        else:
            self.__p = GPIO.PWM(enable, 50)
            self.__p.start(100)

    def __del__(slef):
        GPIO.cleanup()

    def __change_speed(self, speed):
        if self.__pwm:
            self.__p.ChangeDutyCycle(speed)

    def stop(self):
        GPIO.output((self.__in1, self.__in2), GPIO.LOW)
        self.__change_speed(100)

    def foreward(self, speed=100):
        GPIO.output(self.__in1, GPIO.HIGH)
        GPIO.output(self.__in2, GPIO.LOW)
        self.__change_speed(speed)

    def backward(self, speed=100):
        GPIO.output(self.__in1, GPIO.LOW)
        GPIO.output(self.__in2, GPIO.HIGH)
        self.__change_speed(speed)
    

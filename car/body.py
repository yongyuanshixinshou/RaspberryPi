from wheel import Wheel


class Body:
    def __init__(self, pwm=False):
        self.__left_wheel = Wheel(11, 13, 15, pwm=pwm)
        self.__right_wheel = Wheel(19, 21, 23, pwm=pwm)

    def foreward(self, speed=100):
        self.__left_wheel.foreward(speed)
        self.__right_wheel.foreward(speed)

    def backward(self, speed=100):
        self.__left_wheel.backward(speed)
        self.__right_wheel.backward(speed)

    def left(self, speed=50):
        self.__left_wheel.backward(speed)
        self.__right_wheel.foreward(speed)

    def right(self, speed=50):
        self.__left_wheel.foreward(speed)
        self.__right_wheel.backward(speed)

    def stop(self):
        self.__left_wheel.stop()
        self.__right_wheel.stop()

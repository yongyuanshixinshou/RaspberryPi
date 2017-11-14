#! /usr/bin/python3

from body import Body
from redis import Redis


body = Body(pwm=True)

def control(direction):
    direction_dict = {
            b'foreward': body.foreward,
            b'backward': body.backward,
            b'left': body.left,
            b'right': body.right,
            b'stop': body.stop
            }
    return direction_dict.get(direction, lambda: "nothing")()

if __name__ == '__main__':
    try:
        redis = Redis(password='00000000')
        sub = redis.pubsub()
        sub.subscribe("direction")
        for i in sub.listen():
            if i['type'] == 'message':
                control(i['data'])

    except KeyboardInterrupt:
        pass


import math
import time

from machine import PWM, Pin

# LED embedded on board
pwm = PWM(Pin(25))


def sin_wave():
    for degree in range(0, 360):
        seed = math.sin(math.radians(degree))

        pwm.duty_u16(int(abs(seed * 65535 * 0.95)))
        time.sleep_ms(10)


while True:
    sin_wave()

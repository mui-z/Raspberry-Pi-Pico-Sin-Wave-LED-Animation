import math
import time

from machine import PWM, Pin

# LED embedded on board
pwm = PWM(Pin(25))


def sin_wave():
    for degree in range(0, 90):
        seed = math.sin(math.radians(degree))

        pwm.duty_u16(int(seed * 65535 * 0.8))
        time.sleep_ms(10)

    for degree in range(90, 0, -1):
        seed = math.sin(math.radians(degree))

        pwm.duty_u16(int(seed * 65535 * 0.8))
        time.sleep_ms(10)


while True:
    sin_wave()

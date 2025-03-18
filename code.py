"""
Created by: Osamah
Created on: FEB 2025
Created for: TEJ3M-Unit 2-05 servo angle change
"""

import time
import board
import pwmio
from adafruit_motor import servo

# Setup PWM on GP0
pwm = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

while True:
    my_servo.angle = 0   # Move to 0 degrees
    time.sleep(1)
    my_servo.angle = 90  # Move to 90 degrees
    time.sleep(1)
    my_servo.angle = 180 # Move to 180 degrees
    time.sleep(1)

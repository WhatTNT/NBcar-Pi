import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

p1 = GPIO.PWM(18, 240)
p2 = GPIO.PWM(17, 240)
p1.start(0)
p2.start(60)
try:
    while 1:
        for dc in range(0, 60):
            p1.ChangeDutyCycle(dc)
            p2.ChangeDutyCycle(60 - dc)
            time.sleep(0.01)
        for dc in range(60, 0, -1):
            p1.ChangeDutyCycle(dc)
            p2.ChangeDutyCycle(60 - dc)
            time.sleep(0.01)
except KeyboardInterrupt:
    pass

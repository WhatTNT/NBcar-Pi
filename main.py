# socket connect
import socket

s = socket.socket()
# s.connect(("192.168.31.84", 3000))
# s.connect(("192.168.31.132", 3000))

# gpio starts
import RPi.GPIO as GPIO

FREQUENCY = 120

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.cleanup()

left_forward = GPIO.PWM(18, FREQUENCY)
left_backward = GPIO.PWM(17, FREQUENCY)
right_forward = GPIO.PWM(22, FREQUENCY)
right_backward = GPIO.PWM(23, FREQUENCY)
left_forward.start(0)
left_backward.start(0)
right_forward.start(0)
right_backward.start(0)

while True:
    left_forward.ChangeDutyCycle(100)
    left_backward.ChangeDutyCycle(0)
    right_backward.ChangeDutyCycle(100)
    right_forward.ChangeDutyCycle(0)

# while True:
#     data = s.recv(1024)
#     speed = (int(data[3]) - 100, int(data[4]) - 100)
#     print(speed)
#     if speed[0] < 0:
#         left_backward.ChangeDutyCycle(-speed[0])
#         left_forward.ChangeDutyCycle(0)
#     else:
#         left_forward.ChangeDutyCycle(speed[0])
#         left_backward.ChangeDutyCycle(0)
#
#     if speed[1] < 0:
#         right_backward.ChangeDutyCycle(-speed[1])
#         right_forward.ChangeDutyCycle(0)
#     else:
#         right_forward.ChangeDutyCycle(speed[1])
#         right_backward.ChangeDutyCycle(0)

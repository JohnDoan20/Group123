import RPi.GPIO as GPIO
import time
import PiGGPIOFactory
import Servo
import math
#set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

factory = PiGGPIOFactory()

GPIO.setup(11,GPIO.OUT)  #set pin 11 as output
servo = GPIO.PWM(11,50,pin_factory=factory)  #pin 11, 50 Hz

while True:
    for i in range(0,360):
        servo.value = math.sin(math.radians(i))
        sleep(0.01)

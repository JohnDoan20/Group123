import RPi.GPIO as GPIO
import time
import PiGGPIOFactory
import Servo
import math
#set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)
distance = 67# meters (i dont know the actual circumference of top wooden)
factory = PiGGPIOFactory()
prev_speed=0
GPIO.setup(11,GPIO.OUT)  #set pin 11 as output
servo = GPIO.PWM(11,50,pin_factory=factory)  #pin 11, 50 Hz
#to calculate the speed at which the servo moved we need to check the start time and the end time
while True:
    seconds = time.time()
    #print("Seconds since epoch =", seconds) 
    start = seconds
    for i in range(0,360):
        servo.value = math.sin(math.radians(i))
        time.sleep(0.01)
    end= time.time
    
    time_elapsed=end-start #calculate
    speed=distance/time_elapsed
    print('speed used for revolution is : ',speed)
    if prev_speed<speed:
        prev_speed=speed
    print('fastest speed used for revolution is : ',speed)

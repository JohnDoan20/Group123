import RPi.GPIO as GPIO
import time
#set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)  #set pin 11 as output
servo = GPIO.PWM(11,50)  #pin 11, 50 Hz

servo.start(0)           #initially, the servo is off
print ("Waiting for 2 seconds")
time.sleep(2)

print ("Rotating 180 degrees in 10 steps")
duty = 2

#looping from 2 to 12(0 to 180 degrees)
while duty <= 12:
    servo.ChangeDutyCycle(duty)
    time.sleep(1)
    duty = duty + 1

#wait a couple of seconds
time.sleep(2)

#print ("Turning back to 90 degrees for 2 seconds")
#servo.ChangeDutyCycle(7)
#time.sleep(2)

#turning back to zero
print ("Turning back to 0 degrees")
servo.ChangeDutyCycle(2)
time.sleep(1)
servo.ChangeDutyCycle(0)

#Cleaning things at the end
servo.stop()
GPIO.cleanup()
print ("Everything's cleaned up")

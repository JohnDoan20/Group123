# general libraries
import time
import random

# camera libraries
from picamera import PiCamera, Color

# servo libraries
import RPi.GPIO as GPIO

# load cell libraries
from hx711 import HX711
import sys

# setup:

# camera:
camera = PiCamera()
camera.rotation = 270
camera.resolution = (1080, 1080)

def take_photo(name, preview_time):
    camera.start_preview()
    time.sleep(3+preview_time)
    camera.capture('/home/pi/Desktop/%s.jpg' % name)   #'/home/pi/Desktop/image.jpg'
    camera.stop_preview()
	
def take_video(name, length):
	camera.start_preview()
	camera.start_recording('/home/pi/Desktop/%s.h264' % name)
	time.sleep(3+length)
	camera.stop_recording()
	camera.stop_preview()
	
	
# servo:
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)  #set pin 11 as output
servo = GPIO.PWM(11,50)  #pin 11, 50 Hz

duty = 2 #global variable for servo pos

def start_servo():
    servo.start(0)


def stop_servo():
    servo.stop()

'''
def rotate_servo(angle, direction):
    if direction == True:
    
    

def reset_servo():
    servo.DutyCycleSet(2.5)
    return
'''

# load cell:
hx = HX711(5, 6) # GPIO PINS OF RPI
referenceUnit = 249.134021

hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(referenceUnit)

hx.reset()
hx.tare()

def load_tare():
    hx.tare
    print("tare complete")

    
def get_weight(print_bool):
    weight = hx.get_weight(5)
    if print_bool:
        print(weight)
    return weight
    
def calibrate_ref_unit():
    print("beginning calibration...")
    time.sleep(1)
    print("please place an object of known weight on platform")
    
    cont = input("ready? (y/n)")
    while cont != 'y':
        sleep(1)
        
    knownWeight = float(input("please enter precise weight of object"))
    sleep(1)
    
    val = get_weight(False)
    referenceUnit = val/knownWeight
    
    hx.set_reference_unit(referenceUnit)
    
    print("calibration complete :)")

# general:
def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()
        
    print("Bye!")
    sys.exit()



# main code:

calibrate_ref_unit()

try:
    get_weight(True)    
except (KeyboardInterrupt, SystemExit):
    cleanAndExit()
    



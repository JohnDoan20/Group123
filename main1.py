from picamera import PiCamera, Color
from time import sleep
import random
# camera libraries

# setup:

# camera:
camera = PiCamera()
camera.rotation = 270
camera.resolution = (1080, 1080)

def take_photo(name, preview_time):
	camera.start_preview()
	sleep(3+preview_time)
	camera.capture('/home/pi/Desktop/%s.jpg' % name)   #'/home/pi/Desktop/image.jpg'
	camera.stop_preview()
	
def take_video(name, length):
	camera.start_preview()
	camera.start_recording('/home/pi/Desktop/%s.h264' % name)
	sleep(3+length)
	camera.stop_recording()
	camera.stop_preview()
	

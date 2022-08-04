from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

# camera configuration/settings
camera.rotation = 0
camera.resolution = (2592, 1944)
camera.framerate = 15

# to see preview:
# camera.start_preview(alpha = 255)

# to stop preview:
# camera.stop_preview()

# delay = sleep(<# seconds)


# to take a picture;
pic_num = 0
camera.start_preview()
sleep(3)
camera.capture('/home/Desktop/image%s.jpg' % pic_num)   #'/home/pi/Desktop/image.jpg'
pic_num += 1
camera.stop_preview()

# remember to sleep b/w pictures to allow refocus

# to record video:
#camera.start_preview()
#camera.start_recording('/home/pi/Desktop/video.h264')
#sleep(5)
#camera.stop_recording()
#camera.stop_preview()





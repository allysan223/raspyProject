from picamera import PiCamera
from time import sleep
import sys

camera = PiCamera()

#Start camera preview
camera.start_preview()
#Sleep for atealst 2 seconds to allow sensors to sense light exposure
sleep(5)
#take photo
camera.capture('/home/pi/raspyProject/pics/image.jpg')
camera.stop_preview()
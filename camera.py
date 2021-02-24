from picamera import PiCamera
from time import sleep
import sys
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import printer

def button_callback(channel): #callback will run in another thread when event detected
    print("Button was pushed!")
    takePhoto()
    print("Photo saved!")

def takePhoto():
    #Start camera preview
    camera.start_preview()
    #Sleep for atealst 2 seconds to allow sensors to sense light exposure
    sleep(2)
    #take photo
    camera.capture('/home/pi/raspyProject/pics/image.jpg')
    camera.stop_preview()
    printer.preparePhoto()
    printer.printPhoto()

#Initialize Button
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #PUD_DOWN# Set pin 10 to be an input pin and set initial value to be pulled low (off)
#Set up button push event, regardless of whatever else is happening in the program, the function my_callback will be run
GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge

#Initialize camera
camera = PiCamera()

# do nothing while waiting for button to be pushed
try:  
    while True:
        continue
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup() 

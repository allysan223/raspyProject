from escpos import printer
from escpos.printer import Usb
import cv2
 
img = cv2.imread('pics/image.jpg', cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',img.shape)
 
scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)

p = printer.File("/dev/usb/lp0")
p.text("Test print")
p.barcode('1324354657687', 'EAN13', 64, 2, '', '')
print("barcode")
#p.image("pics/house.jpg")
p.image("pics/luna_crop.png")

print("image printed")
#p.cut()


# with open('/dev/usb/lp0', 'wb') as printer:
#     printer.write("1234567890123456789012345678901234567890\n")
#     printer.write("Line 2\n")
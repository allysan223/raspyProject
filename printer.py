from escpos import printer
from escpos.printer import Usb
import cv2
 
def preparePhoto():
    img = cv2.imread('pics/image.jpg', cv2.IMREAD_UNCHANGED)
    print('Original Dimensions : ',img.shape)
    scale_percent = 10 # percent of original size, width max 384. 385 too big
    while(int(img.shape[0] * scale_percent / 100) < 384.1):
        scale_percent += 1
        # print('percent scaled : ',scale_percent)
        # print('width : ',int(img.shape[0] * scale_percent / 100))
    scale_percent -= 1
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    resized = cv2.rotate(resized, cv2.cv2.ROTATE_90_CLOCKWISE) 
    cv2.imwrite("pics/resize.png", resized) 
    print('Resized Dimensions : ',resized.shape)
    

def printPhoto():
    p = printer.File("/dev/usb/lp0")
    #p.text("Test print")
    #p.barcode('1324354657687', 'EAN13', 64, 2, '', '')
    print("barcode")
    #p.image("pics/house.jpg")
    p.image("pics/resize.png")

    print("image printed")
    #p.cut()


# with open('/dev/usb/lp0', 'wb') as printer:
#     printer.write("1234567890123456789012345678901234567890\n")
#     printer.write("Line 2\n")
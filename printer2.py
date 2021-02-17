from escpos import printer
from escpos.printer import Usb


# Adapt to your needs
p = printer.File("/dev/usb/lp0")
p.text("HELLO TESTTing")
p.barcode('1324354657687', 'EAN13', 64, 2, '', '')
print("barcode")
p.image("pics/house.jpg")
p.image("pics/google.png")
print("image printed")
# p.cut()


# with open('/dev/usb/lp0', 'wb') as printer:
#     printer.write("1234567890123456789012345678901234567890\n")
#     printer.write("Line 2\n")
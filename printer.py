from PIL import Image
from thermalprinter import *

with ThermalPrinter(port='/dev/usb/lp0') as printer:
    # Picture
    #printer.image(Image.open('gnu.png'))

    # Bar codes
    printer.barcode_height(80)
    printer.barcode_position(BarCodePosition.BELOW)
    printer.barcode_width(3)
    printer.barcode('012345678901', BarCode.EAN13)


    # Line feeds
    printer.feed(2)
import sys
import re
from PIL import Image, ImageOps, ImageEnhance 
from io import BytesIO

import pytesseract

REGEX = re.compile(r'(\([^\(\)]+?, [0-9]{4}\))')

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Simple image to string
#print(pytesseract.image_to_string(Image.open(sys.argv[1])))

with open(sys.argv[1], 'rb') as fp:
    #image = Image.open(BytesIO(fp.read()))
    image = Image.open(sys.argv[1])

if image.mode == 'RGBA':
    r,g,b,a = image.split()
    image = Image.merge('RGB', (r,g,b))

image = ImageOps.invert(image)

contrast = ImageEnhance.Contrast(image)
image = contrast.enhance(2)

config = ("--psm 6")
image = image.rotate(270, Image.NEAREST, expand = 1)
image.save("outpic.jpg", "JPEG")

txt = pytesseract.image_to_string(image, config = config)
txt = " ".join([line.strip() for line in txt.split('\n')])
for line in REGEX.findall(txt):
    print(line)

#print(txt)
import sys
import re
from PIL import Image, ImageOps, ImageEnhance 
from io import BytesIO

import pytesseract

REGEX = re.compile(r'(\([^\(\)]+?, [0-9]{4}\))')

def ocr_page(filename, rotate=True):

    image = Image.open(filename)

    if image.mode == 'RGBA':
        r,g,b,a = image.split()
        image = Image.merge('RGB', (r,g,b))

    image = ImageOps.invert(image)

    contrast = ImageEnhance.Contrast(image)
    image = contrast.enhance(2)

    # needed for original photo, cropped doesn't work with it
    if rotate: image = image.rotate(270, Image.NEAREST, expand = 1)
    image.save("outpic.jpg", "JPEG")

    config = ("--psm 6")
    txt = pytesseract.image_to_string(image, config = config)
    txt_single_line = " ".join([line.strip() for line in txt.split('\n')])
    results = REGEX.findall(txt_single_line)
    
    return results

def main():

    res = ocr_page(sys.argv[1], rotate=False)
    for line in res: print(line)

if __name__ == '__main__':
    main()
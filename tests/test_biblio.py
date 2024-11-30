import pytest
import biblio

# TODO this is not actually the correct OCR for the page! we are missing:     
#          (2 vols., Westport, Conn., 1985) after (Oxford, 1988)
#          (Paris, 1987) after (London, 1989)
#          (London, 1961) after (New York, 1944)
# but this is the best we have rn so it's gonna be the test case until the code is good enough to improve its tests :)
def test_basic_ocr():
    results = ["(Berkeley, 1984)",
               "(Oxford, 1987)",
               "(Oxford, 1988)",
               "(London, 1989)",
               "(Paris, 1974)",
               "(New York, 1944)",
               "(London, 1988)",
               "(New York and London, 1985)"]
    filename = 'data\\IMG_2075_cropped.jpg'
    assert biblio.ocr_page(filename, rotate=False) == results
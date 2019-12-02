import re

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def date_convert(text):
    month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10,
                  'Nov': 11, 'Dec': 12}

    if text.find('Jan' or 'Feb' or 'Mar' or 'Apr' or 'May' or 'Jun' or 'Jul' or 'Aug' or 'Sep' or 'Oct' or
                 'Nov' or 'Dec'):
        text.replace('Jan' or 'Feb' or 'Mar' or 'Apr' or 'May' or 'Jun' or 'Jul' or 'Aug' or 'Sep' or 'Oct' or
                     'Nov' or 'Dec')


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and

    date_regexs = [r'\d{2}(/|-|,)\d{2}(/|-|,)\d{4}', r'\d{2}(/|-|,)\d{2}(/|-|,)\d{2}', r'(\b\d{1,2}\D{0,3})?\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(Nov|Dec)(?:ember)?)\D?(\d{1,2}\D?)?\D?((19[7-9]\d|20\d{2})|\d{2})']
    match = None
    for regex in date_regexs:
        match = re.search(regex, text)

        if match is not None:
            break

    print("text: ", text)

    if match is not None:
        return text, str(f"date: {match}")
    else:
        return text, str("date: null")

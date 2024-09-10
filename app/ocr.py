import easyocr

def extract_text_from_image(image_path, lang='ja'):
    reader = easyocr.Reader([lang], gpu=True)
    return reader.readtext(image_path)

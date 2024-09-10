import easyocr

from app.log import log

class OCR:
    def __init__(self, language):

        log(f'Iniciando o OCR com idioma {language}')

        self.reader = easyocr.Reader([language])

    def read_text(self, frame_file):

        log(f'Lendo texto da imagem {frame_file}')

        result = self.reader.readtext(frame_file)
        return result
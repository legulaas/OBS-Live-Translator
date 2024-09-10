from deep_translator import GoogleTranslator

def translate_text(text, dest_language='pt'):
    translator = GoogleTranslator(target=dest_language)
    return translator.translate(text)

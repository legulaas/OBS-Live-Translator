import os

from glob import glob
from PIL import Image, ImageDraw
from pynput import keyboard

# Importa funções
from app.translation import translate_text
from app.overlay import add_overlay
from app.log import log
from app.utils import limpar_frames

# Importa as classes 
from app.obs import OBS
from app.ocr import OCR

# Inicia WebSocket com OBS
obs = OBS("localhost", 4444, "123456")

# Instancia o OCR (Optical Character Recognition)
ocr = OCR('ja')

def on_press(key):

	if key == keyboard.Key.insert:

		log('Tecla Insert pressionada. Iniciando leitura e tradução de conteúdo...')

		screenshot_res = obs.save_screenshot()
		ocr_tradutor(screenshot_res)

	elif key == keyboard.Key.delete:
		
		log('Tecla Delete pressionada. Limpando frames...')
		limpar_frames()
		if os.path.exists('overlay.png'):
			os.remove('overlay.png')
		log('Frames limpos com sucesso!\n')

	elif key == keyboard.Key.f12:
		log('Encerrando o programa com tecla F12')
		exit()

def ocr_tradutor(res):

	log('Iniciando processamento de imagem...')

	img_fns = glob('./frames/*.png')

	image = Image.new('RGBA', res, (0, 0, 0, 0))
	draw = ImageDraw.Draw(image)

	results = ocr.read_text(img_fns[0])

	for bbox, text, _ in results:
		translated_text = translate_text(text)
		if translated_text:
			add_overlay(draw, bbox, translated_text)

	# Salvar a imagem com sobreposição
	image.save('overlay.png', 'PNG')

	if (image):
		log('Imagem processada com sucesso!\n')

def main():
    # Monitorando o teclado em segundo plano
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()





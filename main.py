import pandas as pd
import os
import cv2

from glob import glob
from PIL import Image, ImageDraw
from pynput import keyboard
from time import sleep

from app.ocr import extract_text_from_image
from app.translation import translate_text
from app.overlay import add_overlay
from app.log import log
from app.obs import OBS

# Inicia WebSocket com OBS
obs = OBS("localhost", 4444, "123456")

width = 1920
height = 1080

def save_first_frame(video_path, output_image_path):
    # Carrega o vídeo
    video = cv2.VideoCapture(video_path)

    # Verifica se o vídeo foi carregado corretamente
    if not video.isOpened():
        print(f"Erro ao abrir o vídeo {video_path}")
        return

    # Lê o primeiro frame
    success, frame = video.read()

    if success:
        # Salva o frame como uma imagem PNG
        cv2.imwrite(output_image_path, frame)
        print(f"Primeiro frame salvo como {output_image_path}")
    else:
        print("Não foi possível ler o primeiro frame.")

    # Fecha o vídeo
    video.release()

def limpar_frames(formato=""):

	if formato != "":
		for f in glob('./frames/*.'+formato):
			os.remove(f)
	else:
		for f in glob('./frames/*'):
			os.remove(f)

def on_press(key):

	if key == keyboard.Key.scroll_lock:

		# Limpa os frames anteriores
		limpar_frames()

		obs.start_recording()
		sleep(1)
		obs.stop_recording()

		while not glob('./frames/*'):
			sleep(1)
		sleep(2)

		# Salva o primeiro frame como imagem
		save_first_frame(glob('./frames/*')[0], './frames/frame.png')

		# Deleta o .mp4
		limpar_frames("mp4")

		log('Tecla Scroll Lock pressionada. Iniciando OCR e tradução...')

		ocr_tradutor()

	elif key == keyboard.Key.pause:
		log('Tecla Pause pressionada. Limpando frames...')
		limpar_frames()
		if os.path.exists('overlay.png'):
			os.remove('overlay.png')
		log('Frames limpos com sucesso!\n')

	elif key == keyboard.Key.f12:
		log('Encerrando o programa com tecla F12')
		exit()

def ocr_tradutor():

	log('Iniciando processamento de imagem...')

	img_fns = glob('./frames/*.png')

	# Cria uma nova imagem em branco para overlay
	image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
	draw = ImageDraw.Draw(image)

	# Processar imagem
	log (f'Processando imagem {img_fns[0]}...')
	results = extract_text_from_image(img_fns[0])

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





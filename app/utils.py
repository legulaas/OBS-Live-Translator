import os
import cv2

from PIL import Image, ImageDraw
from glob import glob


def textsize(text, font):
    im = Image.new(mode="P", size=(0, 0))
    draw = ImageDraw.Draw(im)
    _, _, width, height = draw.textbbox((0, 0), text=text, font=font)
    return width, height

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

def get_resolution(video_path):
    video = cv2.VideoCapture(video_path)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    return width, height

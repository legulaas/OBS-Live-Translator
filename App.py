import pandas as pd
import numpy as np

from glob import glob
from tqdm.notebook import tqdm
from deep_translator import GoogleTranslator
from PIL import Image, ImageDraw, ImageFont

import matplotlib.pyplot as plt
from PIL import Image

import easyocr

plt.style.use('ggplot')

img_fns = glob('./frames/*')

# Mostra a imagem que está sendo processada
# fig, ax = plt.subplots(figsize=(10, 10))
# ax.imshow(plt.imread(img_fns[3]))
# ax.axis('off')
# plt.show()

def translate_text(text, dest_language='pt'):
    translator = GoogleTranslator(target=dest_language)
    translation = translator.translate(text)
    return translation

def textsize(text, font):
    im = Image.new(mode="P", size=(0, 0))
    draw = ImageDraw.Draw(im)
    _, _, width, height = draw.textbbox((0, 0), text=text, font=font)
    return width, height

def draw_rounded_rectangle(draw, xy, radius, fill):
    x0, y0, x1, y1 = xy
    draw.rectangle([x0 + radius, y0, x1 - radius, y1], fill=fill)
    draw.rectangle([x0, y0 + radius, x1, y1 - radius], fill=fill)
    draw.pieslice([x0, y0, x0 + 2 * radius, y0 + 2 * radius], 180, 270, fill=fill)
    draw.pieslice([x1 - 2 * radius, y0, x1, y0 + 2 * radius], 270, 360, fill=fill)
    draw.pieslice([x0, y1 - 2 * radius, x0 + 2 * radius, y1], 90, 180, fill=fill)
    draw.pieslice([x1 - 2 * radius, y1 - 2 * radius, x1, y1], 0, 90, fill=fill)

def add_overlay(bbox, translated_text):
    
    # Calcular largura e altura do bbox
    width = bbox[1][0] - bbox[0][0]
    height = bbox[2][1] - bbox[0][1]
    
    # Encontrar o ponto central do bbox
    center_x = bbox[0][0] + width / 2
    center_y = bbox[0][1] + height / 2
        
    # Configurar a fonte (ajustar o tamanho da fonte conforme necessário)
    font = ImageFont.truetype("arial.ttf", int(height * 0.8))  # Ajuste do tamanho da fonte
        
    text_width, text_height = textsize(translated_text, font)
    
    # Calcular a nova posição para centralizar o texto traduzido
    new_x = center_x - text_width / 2
    new_y = center_y - text_height / 2
    
    # Calcular a área do retângulo de fundo
    background_area = (new_x, new_y, new_x + text_width, new_y + text_height)
    
    # Desenhar o retângulo de fundo com 50% de opacidade
    draw.rectangle(background_area, fill=(0, 0, 0, 128))  # Preto com 50% de opacidade
    
    # Desenhar o texto traduzido na posição centralizada
    draw.text((new_x, new_y), translated_text, font=font, fill=(255, 255, 255, 255))  # Cor branca para visibilidade

reader = easyocr.Reader(['ja'], gpu = True)

results = reader.readtext(img_fns[3])

pd.DataFrame(results, columns=['bbox','text','conf'])

# Criar uma nova imagem (exemplo para o tamanho do frame do OBS)
image = Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
draw = ImageDraw.Draw(image)

for i in range(len(results)): 
    bbox = results[i][0]
    text = results[i][1]

    translated_text = translate_text(text)
    
    if translated_text is None:
        continue  # Vai para a próxima iteração do loop


    add_overlay(bbox, translated_text)

# Salvar ou enviar esta imagem para ser usada no OBS como sobreposição
image.save('overlay.png')
if(image):
    print('Imagem salva com sucesso!')
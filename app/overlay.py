from PIL import Image, ImageDraw, ImageFont
from app.utils import textsize

def add_overlay(draw, bbox, translated_text, font_path="arial.ttf"):
    width = bbox[1][0] - bbox[0][0]
    height = bbox[2][1] - bbox[0][1]
    
    center_x = bbox[0][0] + width / 2
    center_y = bbox[0][1] + height / 2
    
    font = ImageFont.truetype(font_path, int(height * 0.8))
    text_width, text_height = textsize(translated_text, font)
    
    new_x = center_x - text_width / 2
    new_y = center_y - text_height / 2
    
    background_area = (new_x, new_y, new_x + text_width, new_y + text_height)
    draw.rectangle(background_area, fill=(0, 0, 0, 220))
    draw.text((new_x, new_y), translated_text, font=font, fill=(255, 255, 255, 255))

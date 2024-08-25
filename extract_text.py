import easyocr
import cv2
import matplotlib.pyplot as plt
import requests
import numpy as np

# Crie um leitor de OCR com o idioma desejado
reader = easyocr.Reader(['pt'])  # 'en' para inglês; adicione outros idiomas se necessário

# Caminho para a imagem - use o link direto para a imagem
image_url = 'https://github.com/RickTurion/ImagesText/blob/main/inputs/linux.jpg?raw=true'

# Baixar a imagem
response = requests.get(image_url)
image_arr = np.array(bytearray(response.content), dtype=np.uint8)
image = cv2.imdecode(image_arr, -1)

# Extraia texto da imagem
results = reader.readtext(image)

# Desenhe as caixas delimitadoras e o texto na imagem
for (bbox, text, prob) in results:
    (top_left, top_right, bottom_right, bottom_left) = bbox
    (top_left_x, top_left_y) = top_left
    (bottom_right_x, bottom_right_y) = bottom_right
    cv2.rectangle(image, (int(top_left_x), int(top_left_y)),
                  (int(bottom_right_x), int(bottom_right_y)), (0, 255, 0), 2)
    cv2.putText(image, text, (int(top_left_x), int(top_left_y) - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Converta a imagem de BGR para RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Exiba a imagem com o texto extraído usando matplotlib
plt.imshow(image_rgb)
plt.axis('off')  # Remove os eixos
plt.show()

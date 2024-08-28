import urllib.request
import cv2
import numpy as np
import easyocr
import os
from tabulate import tabulate

# URL da imagem
url = 'https://raw.githubusercontent.com/RickTurion/ImagesText/main/inputs/Imagem1.jpg'

# Caminho para salvar a imagem localmente
local_image_path = 'input/imagem1.jpg'

# Diretório onde a imagem será salva
os.makedirs(os.path.dirname(local_image_path), exist_ok=True)

# Baixar a imagem
try:
    response = urllib.request.urlopen(url)
    image_data = response.read()
    
    # Salvar a imagem localmente
    with open(local_image_path, 'wb') as f:
        f.write(image_data)
    
    print("Imagem baixada e salva com sucesso.")
except Exception as e:
    raise ValueError(f"Erro ao baixar a imagem: {e}")

# Carregar a imagem
image = cv2.imread(local_image_path)

if image is None:
    raise ValueError("A imagem não pôde ser carregada. Verifique o caminho do arquivo.")

print("Imagem carregada com sucesso.")

# Configurar o OCR
reader = easyocr.Reader(['en'])

# Extrair texto da imagem
result = reader.readtext(local_image_path)

# Formatando a saída
if result:
    table = []
    for detection in result:
        table.append([detection[1], f"{detection[2]:.2f}"])

    print("\nTexto extraído da imagem:")
    print(tabulate(table, headers=["Texto", "Confiança"], tablefmt="grid"))
else:
    print("Nenhum texto foi encontrado na imagem.")

# Opcional: Mostrar a imagem usando OpenCV
# cv2.imshow('Imagem', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

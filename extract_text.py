import easyocr
import cv2
import matplotlib.pyplot as plt

# Crie um leitor de OCR com o idioma desejado
reader = easyocr.Reader(['pt'])

# Caminho para a imagem no repositório
image_path = '/workspaces/ImagesText/input/linux.jpg'  # Certifique-se de que o caminho está correto

# Carregue a imagem usando OpenCV
image = cv2.imread(image_path)

# Verifique se a imagem foi carregada corretamente
if image is None:
    raise ValueError("A imagem não pôde ser carregada. Verifique o caminho do arquivo.")

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

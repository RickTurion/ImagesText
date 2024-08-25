import urllib.request

# URL da imagem
url = 'https://raw.githubusercontent.com/RickTurion/ImagesText/main/inputs/linux.jpg'
local_filename = 'linux.jpg'

# Baixar a imagem
urllib.request.urlretrieve(url, local_filename)

# Carregar a imagem
image = cv2.imread(local_filename)

if image is None:
    raise ValueError("A imagem não pôde ser carregada. Verifique o caminho do arquivo.")
else:
    print("Imagem carregada com sucesso.")

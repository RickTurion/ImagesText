# Projeto OCR - Extração de Texto de Imagens

 Este repositório contém um exemplo de como usar OCR para extrair texto de imagens. Usaremos o módulo EasyOCR junto com Python para esse propósito.

## Índice

1. [Introdução](#introdução)
2. [Requisitos](#requisitos)
3. [Como Usar](#como-usar)
5. [Exemplos de saída](#exemplos-de-uso)
6. [Referências](#referências)

## Introdução

 O Reconhecimento Óptico de Caracteres (OCR) é uma tecnologia que permite a conversão de diferentes tipos de documentos, como arquivos digitalizados, PDFs ou fotos capturadas por uma câmera, em dados editáveis e pesquisáveis. Neste projeto, vamos utilizar o EasyOCR para extrair textos de imagens. Eu usei para efetuar a atividade os mesmos passos que vou descrever abaixo, assim pode ser que alguem possa fazer uso do mesmo caso aceito. o/

## Requisitos

- Python 3.7 ou superior
- Módulo EasyOCR
- Bibliotecas Python: `Numpy`, `easyocr`, `opencv-python-headless`,`tabulate`

## Como usar

### Usando o EasyOCR

 Antes de começar, é necessário instalar o **EasyOCR**. No exemplo será usado via **Codespace** diretamente no Github devido a eu estar com um computador de trabalho e não irei instalar, pois tenho limitações de instalação. Fique a vontade para fazer do seu jeito, conforme ensinado e disposto pela Elidiana Andrade nos tópicos do curso : Versionamento de Código com Git e GitHub.

**Para Windows:**

 Requer a instalação de requisitos. Clique [aqui](https://www.jaided.ai/easyocr/install/#:~:text=Pre-install%20%28for%20Windows%29%201%201.%20From%20pip%20package,by%20%24%20pip%20install%20git%2Bgit%3A%2F%2Fgithub.com%2Fjaidedai%2Feasyocr.git%203%203.%20Docker) e siga as instruções.

**Para uso via Codespace:**

**Passo 1** - Crie um novo repositório conforme solicitado no desafio da DIO, com o nome que quiser. No meu exemplo usarei o ImagesText.

**Passo 2** - Crie uma pasta Inputs. Procure na internet algumas imagens que contenham textos, de preferência imagens mais limpas, sem muita informação neste primeiro momento para que o recurso funcione de forma mais assertiva. Você também pode tirar fotos de livros ou algo que contenha textos como placas de locais de interesse, campanhas políticas etc. Faça upload delas de preferência em formato jpg para a pasta Inputs.

**Passo 3** - Crie uma segunda pasta dentro da raiz do seu repositório criado no passo 1, com o nome **Output**. Nela você irá fazer o upload das saídas como evidências para a entrega do projeto.

**Passo 4** - Na raiz do repositório criado no passo 1 crie um arquivo chamado **extract_text.py**. Nele insira o conteudo abaixo:
Obs: Altere as pastas **local_image_path = ''** e **url = ''** para os caminhos das suas imagens. Coloque a imagem que o EasyOCR irá ler. Se precisarem de um exemplo vejam o meu: [aqui](https://github.com/RickTurion/ImagesText/blob/main/extract_text.py)

```bash
import urllib.request
import cv2
import numpy as np
import easyocr
import os
from tabulate import tabulate

# URL da imagem
url = '***'

# Caminho para salvar a imagem localmente
local_image_path = '***'

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
```
Passo 5 - Ainda na raíz crie um segundo arquivo chamado requirements.txt. Nele insira as linhas abaixo. Esse arquivo irá instalar os recursos necessários automaticamente para que nosso lab funcione.
```bash
easyocr
opencv-python-headless
numpy
tabulate
```
**Passo 6** - Agora que já criamos o script em python e os arquivos que precisaremos, no seu repositório inicial (passo 1) clique em "Code" ( Botão verde), vá em Codespaces, e clique no (+). Irá abrir a tela de terminal onde executaremos o script.

**Passo 7** - Certifique-se que está no seu repositório criado (workspace/*seu repositório*).

**Passo 8** - Após a instalação dos recursos necessários, execute o script criado no passo 4.
```bash
pyhon extract_text.py
```
**Passo 9** - Se tudo tiver dado certo o script irá trazer tabulado os dados de texto da imagem escolhida por você para que o EasyOCR lê-se, contendo seu grau de confiança, onde quanto maior mais assertivo.

## Exemplos de saída

Exemplo:

```markdown
Texto extraído da imagem:
+----------------------+-------------+
| Texto                |   Confiança |
+======================+=============+
| Fundamentos, Pratica |        0.99 |
+----------------------+-------------+
| LINUX                |        1    |
+----------------------+-------------+
| Certificacao LPI     |        0.88 |
+----------------------+-------------+
| Exame 117-102        |        0.93 |
+----------------------+-------------+
| Fundamentos, Pratica |        0.8  |
+----------------------+-------------+
| LINUX                |        0.84 |
+----------------------+-------------+
| & Certificacao LPI   |        0.56 |
+----------------------+-------------+
| Exame 117-101        |        0.92 |
+----------------------+-------------+
```

## Referências

#### Aulas DIO - BootCamp Copilot IA

- Aplicações e Impacto da IA no Mundo Atual - [Aplicações e Impacto da IA no Mundo Atual](https://web.dio.me/course/aplicacoes-e-impacto-da-ia-no-mundo-atual/learning/442a4379-a52e-4968-88a5-b93d818da63e?back=/track/microsoft-copilot-ai&tab=undefined&moduleId=undefined) - Felipe Aguiar

- Versionamento de Código com Git e GitHub - [Versionamento de Código com Git e GitHub](https://github.com/elidianaandrade/dio-curso-git-github) - Elidiana Andrade

- Visão Computacional - [Visão Computacional](https://web.dio.me/course/visao-computacional/learning/a3d1e2a4-4437-44c0-84b4-421a2977d50f?back=/track/microsoft-copilot-ai&tab=undefined&moduleId=undefined) - Diego Renan

- Desafios de Projetos: Crie Um Portfólio Vencedor - [Desafios de Projetos: Crie Um Portfólio Vencedor](https://web.dio.me/course/desafios-de-projetos-crie-um-portfolio-vencedor/learning/37bfd7e4-fadd-48c2-831b-a95f84d244db?back=/track/microsoft-copilot-ai&tab=undefined&moduleId=undefined) - Venilton Falvo Jr

- Desafios de Código: Aperfeiçoe Sua Lógica e Pensamento Computacional - [Desafios de Código: Aperfeiçoe Sua Lógica e Pensamento Computacional](https://web.dio.me/course/desafios-de-codigo-aperfeicoe-sua-logica-e-pensamento-computacional/learning/0742edea-d41f-4584-a8bb-d5e9866fb019?back=/track/microsoft-copilot-ai&tab=undefined&moduleId=undefined)) - Venilton Falvo Jr

- Ajustes nos códigos em Python - [GPT](https://chatgpt.com/) - IA

##Importante: Não se esqueçam de dar Commit e reload no terminal caso estejam usando somente o terminal Web como eu, e também instalar os complementos no Browser quando solicitado.
Todo o conteúdo do Bootcamp oferecido pela DIO e Microsoft foi de grande valia para entendimento e atualização no conhecimento de IA, trazendo um upgrade de skills ótimo para os profissionais que queiram integrar os recursos aos seus trabalhos, empresas e dia a dia.

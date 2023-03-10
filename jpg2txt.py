import pytesseract
import cv2

# passo 1: ler a imagem
imagem = cv2.imread("media/teste.png")

# passo 2: pedir pro tessaract extrair o texto da imagem
texto = pytesseract.image_to_string(imagem, lang="por")

print(texto)

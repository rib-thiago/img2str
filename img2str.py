import argparse
import pytesseract
import cv2


def extract_text(filename, language):
    # passo 1: ler a imagem
    imagem = cv2.imread(filename)

    # passo 2: pedir pro tessaract extrair o texto da imagem
    texto = pytesseract.image_to_string(imagem, lang=language)

    # passo 3: imprimir a resposta na tela
    print(texto)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract text from an image")
    parser.add_argument("filename", help="path to the image file")
    parser.add_argument("--language", "-l", default="eng", help="language code for OCR")

    args = parser.parse_args()

    extract_text(args.filename, args.language)


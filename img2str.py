import argparse
import pytesseract
import cv2
from textblob import TextBlob


def extract_text(filename, language, dest_language):
    # Mapeia os códigos de idiomas entre o Tesseract e o TextBlob
    lang_map = {
        "por": "pt",
        "eng": "en",
        "rus": "ru",
        "spa": "es",
        "deu": "de",
        "chi_sim": "zh-CN",
        "jpn": "ja",
        "fra": "fr",
        "ara": "ar"
    }

    # passo 1: ler a imagem
    imagem = cv2.imread(filename)

    # passo 2: pedir pro tessaract extrair o texto da imagem
    texto = pytesseract.image_to_string(imagem, config='--psm 4', lang=language)

    tb = TextBlob(texto)
    translated = tb.translate(from_lang=lang_map[language], to=lang_map[dest_language])

    # passo 3: imprimir a resposta na tela
    print("ORIGINAL")
    print("=" * 20)
    print(texto)
    print()

    print(f"TRANSLATED ({dest_language.upper()})")
    print("=" * 20)
    print(f"Translated: {translated}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract text from an image")
    parser.add_argument("filename", help="path to the image file")
    parser.add_argument("--language", "-l", default="eng", help="language code for OCR")
    parser.add_argument("--dest-language", "-d", default="en", help="destination language code for translation")

    args = parser.parse_args()

    extract_text(args.filename, args.language, args.dest_language)



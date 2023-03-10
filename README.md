# _img2str_ - Extrator de texto de imagem com tradução

Este script extrai texto de uma imagem usando Tesseract OCR e o traduz usando TextBlob.

## Dependências

- [pytesseract]
- [opencv-python]
- [textblob]

## Pré Instalação

Para usar o tesseract OCR e ter suporte para idiomas diferentes do inglês, é preciso innstalar no computador os pacotes [Tesseract OCR] e o [tessdata]. As instruções a seguir são baseadas no sistema operacional Ubuntu 22.04 lts e maiores informações ou procedimentos específicos podem ser consultados na página dos repositórios.

1. Instale o Tesseract OCR:

```bash
sudo apt install sudo apt install tesseract-ocr libtesseract-dev
```

2. Instale o pacote tessdata:

```bash
sudo apt tesseract-ocr-[lang]
```

Substitua [lang] pelo idioma que você deseja instalar. Alternativamente, baixe o repositório com todas as linguagens:

```bash
https://github.com/tesseract-ocr/tessdata.git
```

3. Defina a variável de ambiente TESSDATA*PREFIX no seu arquivo *~/.bashrc*. Por exemplo, se o diretório tessdata estiver localizado em */usr/share/tesseract-ocr/4.00/tessdata*, adicione a seguinte linha ao final do seu arquivo *~/.bashrc\_:

```bash
export TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/
```

## Uso

1. Instalar dependências usando `pip install -r requirements.txt`
2. Execute o script com o comando `python3 extract_text.py filename.png -l por -d eng`

   - `-l` ou `--language` pode ser usado para definir o código de idioma para OCR. O padrão é 'eng'.
   - `-d` ou `--dest-language` pode ser usado para definir o código do idioma de destino para tradução. O padrão é 'en'.

O script atualmente suporta os seguintes idiomas:

- português (por)
- Inglês (inglês)
- russo (rus)
- Espanhol (spa)
- Alemão (deu)
- Chinês simplificado (chi_sim)
- Japonês (jpn)
- Francês (fra)
- Árabe (ara)

### Exemplo de uso

```python {.line-numbers}
python3 img2str.py example.png -l por -d eng
```

### Output

O script produzirá o texto original e o texto traduzido, formatados da seguinte forma:

```bash
ORIGINAL
====================
[original text]

TRANSLATED (LANGUAGE)
====================
[translated text]
```

[tesseract ocr]: https://github.com/tesseract-ocr/tesseract#installing-tesseract
[tessdata]: https://github.com/tesseract-ocr/tessdata
[pytesseract]: https://pypi.org/project/pytesseract/
[opencv-python]: https://opencv.org/
[textblob]: https://textblob.readthedocs.io/en/dev/

![Banner](https://raw.githubusercontent.com/P0p0vsk1/IMG2ENC/main/banner.jpg)

# <center>Img2Enc: Image-Based Encryption Tool</center>

## Introduction
`Img2Enc` is a Python-based command-line tool that allows users to encrypt and decrypt files using a unique key derived from an image. This tool uses the AES encryption algorithm and offers a user-friendly interface to handle file encryption tasks with ease.

## Features
- Encrypt and decrypt files using AES-256.
- Generate encryption keys from images.
- Command-line interface for easy use.
- Gradient banner display for a visually appealing introduction.

## Installation
> [!IMPORTANT]
> To install Img2Enc, you'll need `Python 3.6` or later.

You can install the required packages using pip:
```bash
pip install -r requirements.txt
```

## Usage
To use `Img2Enc`, navigate to the directory containing the script and run the following commands:
Encryption

```python
python img2enc.py -f <input_file> -o <output_file> -k <keyfile> -e
python img2enc.py -f <input_file> -o <output_file> -i <image> -d
```
> input_file: The file you want to encrypt.

> output_file: The output file where the encrypted data will be saved.

> keyfile: The .key file generated from your image.

> image: The image you want to use as the key

> [!NOTE]
> You have to use -e/-d switches to set the encryption/decryption mode

### Acknowledgments
Thanks to the developers of the `pycryptodome`, `pyfiglet`, and `pillow` libraries.

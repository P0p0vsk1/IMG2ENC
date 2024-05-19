![Banner](https://raw.githubusercontent.com/P0p0vsk1/IMG2ENC/main/banner.jpg)

# <center>Img2Enc: Image-Based Encryption Tool</center>

## Introduction
`Img2Enc` is a Python-based command-line tool that allows users to encrypt and decrypt files using a unique key derived from an image or the image itself. This tool uses the AES encryption algorithm and offers a user-friendly interface to handle file encryption tasks with ease.

## Features
- UnCrackable file encryption
- Encrypt and decrypt files using AES-256.
- Generate encryption keys from images.
- Use either image file or key file to encrypt/decrypt
- Command-line interface for easy use.

## Installation
> [!IMPORTANT]
> To install Img2Enc, you'll need `Python 3.6` or later.

Simply clone this repository:
```bash
git clone https://github.com/P0p0vsk1/IMG2ENC
cd IMG2ENC
```

Then, you can install the required packages using pip:
```bash
pip install -r requirements.txt
```

## Usage
To use `Img2Enc`, navigate to the directory containing the script and simply run `img2enc.py`:

```python
python img2enc.py -f <input_file> -o <output_file> -k <keyfile> -e
python img2enc.py -f <input_file> -o <output_file> -i <image> -d
```
> input_file: The file you want to encrypt.<br>
> output_file: The output file where the encrypted data will be saved.<br>
> keyfile: The .key file generated from your image.<br>
> image: The image you want to use as the key<br>

> [!NOTE]
> You have to use -e/-d switches to set the encryption/decryption mode


> [!WARNING]
> Only jpeg/jpg file formats are supported for image-key-file

### Acknowledgments
Thanks to the developers of the `pycryptodome`, `pyfiglet`, and `pillow` libraries.

import argparse
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import pyfiglet
import img2key

# Constants
BLOCK_SIZE = 16
SALT_SIZE = 16 

# Banner Gradient Function
def print_gradient(text, start_rgb, end_rgb):
    gradient_text = ''
    for i, char in enumerate(text):
        if char == '\n':
            gradient_text += char
            continue
        ratio = i / len(text)
        r = int((end_rgb[0] - start_rgb[0]) * ratio + start_rgb[0])
        g = int((end_rgb[1] - start_rgb[1]) * ratio + start_rgb[1])
        b = int((end_rgb[2] - start_rgb[2]) * ratio + start_rgb[2])
        gradient_text += f'\033[38;2;{r};{g};{b}m{char}'
    return gradient_text + '\033[0m'

# Generate the keyfile
def generate_keyfile(filename):
    try:
        print(f"[+] Generating keyfile for {filename}")
        img2key.generator(filename)
        print(f"[+] Keyfile generated")
    except Exception as e:
        print(f"[-] Error generating keyfile")

# Load keyfile
def load_keyfile(filename):
    try:
        with open(filename, 'rb') as keyfile:
            return keyfile.read()
    except FileNotFoundError:
        print(f"[-] Keyfile {filename} not found")
        raise
    except Exception as e:
        print(f"[-] Error loading keyfile")
        raise

# Encrypt data
def encrypt(data, keyfile):
    try:
        salt = get_random_bytes(SALT_SIZE)
        key = PBKDF2(keyfile, salt, dkLen=32, count=1000)
        cipher = AES.new(key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(data, BLOCK_SIZE))
        return salt + cipher.iv + ciphertext
    except Exception as e:
        print(f"[-] Error encrypting data")
        raise

# Decrypt data
def decrypt(encrypted_data, keyfile):
    try:
        salt = encrypted_data[:SALT_SIZE]
        iv = encrypted_data[SALT_SIZE:SALT_SIZE+BLOCK_SIZE]
        ciphertext = encrypted_data[SALT_SIZE+BLOCK_SIZE:]
        key = PBKDF2(keyfile, salt, dkLen=32, count=1000)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext), BLOCK_SIZE)
        return plaintext
    except Exception as e:
        print(f"[-] Error decrypting data")
        raise

# Padding for block cipher
def pad(data, block_size):
    padding = block_size - len(data) % block_size
    return data + (chr(padding) * padding).encode()

# Remove padding
def unpad(data, block_size):
    padding = data[-1]
    if padding > block_size:
        #raise ValueError("Padding is larger than block size (Invalid key)")
        raise ValueError("Invalid key")
    return data[:-padding]

# Encrypt a file
def encrypt_file(input_file_path, output_file_path, keyfile):
    try:
        print(f"[+] Encrypting {input_file_path}")
        with open(input_file_path, 'rb') as f:
            data = f.read()
        encrypted_data = encrypt(data, keyfile)
        with open(output_file_path, 'wb') as f:
            f.write(encrypted_data)
        print(f"[+] File encrypted: {output_file_path}")
    except Exception as e:
        #print(f"[-] Error encrypting file: {e}")
        raise

# Decrypt a file
def decrypt_file(input_file_path, output_file_path, keyfile):
    try:
        print(f"[+] Decrypting {input_file_path}")
        with open(input_file_path, 'rb') as f:
            encrypted_data = f.read()
        decrypted_data = decrypt(encrypted_data, keyfile)
        with open(output_file_path, 'wb') as f:
            f.write(decrypted_data)
        print(f"[+] File decrypted: {output_file_path}")
    except Exception as e:
        #print(f"[-] Error decrypting file: {e}")
        raise

# Main function
def main():
    f = pyfiglet.figlet_format("Img2Enc", "banner3")
    start_color = (255, 0, 0)
    end_color = (0, 0, 255)
    #print(print_gradient(f, start_color, end_color))
    print(f)
    # -----
    parser = argparse.ArgumentParser(description='File Encryption/Decryption Tool')
    parser.add_argument('-f', '--file', required=True, help='Input file')
    parser.add_argument('-o', '--output', required=True, help='Output file')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-k', '--keyfile', help='.Key file')
    group.add_argument('-i', '--keyimage', help='Key image to generate key file')
    group2 = parser.add_mutually_exclusive_group(required=True)
    group2.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the input file')
    group2.add_argument('-e', '--encrypt', action='store_true', help='Encrypt the input file')

    args = parser.parse_args()

    if args.encrypt == args.decrypt:
        print("[-] Please choose either encryption or decryption mode, not both.")
        return

    keyfile_data = None
    if args.keyfile:
        try:
            keyfile_data = load_keyfile(args.keyfile)
        except Exception as e:
            print(f"[-] Error loading keyfile")
            raise
    elif args.keyimage:
        generate_keyfile(args.keyimage)
        try:
            keyfile_data = load_keyfile(str(args.keyimage.split(".")[0]) + ".key")
        except Exception as e:
            print(f"[-] Error loading keyimage")
            raise

    if args.encrypt:
        output_file_path = args.output
        try:
            encrypt_file(args.file, output_file_path, keyfile_data)
        except Exception:
            return

    if args.decrypt:
        output_file_path = args.output
        try:
            decrypt_file(args.file, output_file_path, keyfile_data)
        except Exception:
            return

if __name__ == '__main__':
    try:
        main()
    except:
        pass

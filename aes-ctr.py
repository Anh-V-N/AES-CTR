#! /usr/bin/env python3

from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
from cryptography.hazmat.backends import default_backend
import os
import sys
import argparse
import hashlib


def Encryptor(plaintext,filename="encrypted"):
    # ENCRYPTOR
    # Generate Key and IV for encrypting
    # Encrypt data and write IV + cipher to a txt file seperated by ":"
    key = os.urandom(32)
    IV = os.urandom(16)
    context = Cipher(algorithms.AES(key),modes.CTR(IV),backend=default_backend())
    cipher = context.encryptor().update(plaintext) + context.encryptor().finalize()
    with open(f"{filename}.hex","w") as f:
        content = IV.hex() + ":" + cipher.hex()
        f.write(content)
    
    with open(f"{filename}.bin","wb") as f:
        content = IV + cipher
        f.write(content)

    print(f'Finished encrypting with key:\n{key.hex()}')
    print(f'The key is needed to decrypt {filename} and will not be displayed again.')



def Decryptor(encrypted):
    # DECRYPTOR
    # Get IV and cipher from encrypted file (same format output from Encryptor), 
    # Decrpyt data using secret key input by user.

    try:
        if ".hex" in encrypted:
            with open(encrypted) as f:
                content = f.read()
            IV, cipher = content.split(":")
            IV = bytes.fromhex(IV)
            print(IV)
            cipher = bytes.fromhex(cipher)
            print(cipher[:16])
            
        elif ".bin" in encrypted:
            with open(encrypted,'rb') as f:
                IV = f.read(16) 
                f.seek(16) # Skip through first 16 bytes
                cipher = f.read()
                
        else:
            print('[ERROR] Invalid file extension. Try ".hex" or ".bin"')
            sys.exit()
        key = input('Enter the key to decrypt: ')
        print(len(key))
        key = bytes.fromhex(key)
        context = Cipher(algorithms.AES(key),modes.CTR(IV),backend=default_backend())
        decrypted = context.decryptor().update(cipher) + context.decryptor().finalize()
        with open('decrypted','wb') as f:
            f.write(decrypted)
    except Exception as e:
        print(f"[ERROR]:{e}")
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encryptor/Decryptor AES-CTR")
    parser.add_argument('-d','--decrypt',help='Decrypt mode',action='store_true')
    parser.add_argument('File/text',help = 'File or text to encrypt/decrypt')
    args = parser.parse_args()

    if args.decrypt:
        Decryptor(sys.argv[2])
    else:
        plaintext = sys.argv[1]
        if os.path.isfile(plaintext):
            with open(plaintext,'rb') as f:
                data = f.read()
            Encryptor(data,plaintext)
        
        else:
            data = plaintext.encode()
            Encryptor(data)
# AES-CTR

Simple python code to encrypt/decrypt file or text using AES-CTR mode.
The key used for encrypting will be display in the console.

Example:
python3 ./aes-ctr.py "This is a secret"
python3 ./aes-ctr.py ./secret.txt
python3 ./aes-ctr.py -d ./secret.txt.bin


```
┌─[anh-ng@parrot]─[~/Desktop/practical-crypto]
└──╼ $./aes-ctr.py -h
usage: aes-ctr.py [-h] [-d] File/text

Encryptor/Decryptor AES-CTR

positional arguments:
  File/text      File or text to encrypt/decrypt

optional arguments:
  -h, --help     show this help message and exit
  -d, --decrypt  Decrypt mode
````

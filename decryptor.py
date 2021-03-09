'''
This module is to decrypt the file and save it to a new file
'''

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

def decrypt(cipherText, password: str, file_name):
    '''
    for decrypting the file
    '''

    #generate the 256bit key from the password
    key = hashlib.sha256(password).digest()

    _iv = cipherText[:16]
    cipherText = cipherText[16:]

    #generate the cipher
    cipher = AES.new(key, AES.MODE_CBC, _iv)

    #decrypt the file and get the plain text
    plainText = unpad(cipher.decrypt(cipherText), AES.block_size)

    with open(file_name, 'wb') as decrypted_file:
        decrypted_file.write(plainText)

if __name__ == "__main__":
    pass

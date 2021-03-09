from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hashlib

def encrypt(file_path: str, password):
    '''
    for encrypting the file
    '''

    #generate the 256bit key from the password
    key = hashlib.sha256(password).digest()

    #generate the cipher
    cipher = AES.new(key, AES.MODE_CBC)

    #read the file
    with open(file_path, 'rb') as original_file:
        plainText = original_file.read()
    
    #encryption
    cipherText = cipher.iv + cipher.encrypt(pad(plainText, AES.block_size))

    return cipherText


if __name__ == "__main__":
    pass

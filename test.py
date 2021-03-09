'''
This module is for testing the file encryptor 
'''

import encryptor, decryptor
import splitter, unsplitter

if __name__ == "__main__":

    #Encrypt and split. The number at the last indicates the number of splitted files. Please choose a number!
    # splitter.split_file(encryptor.encrypt('test_image.png', b'Password'), 5)

    #Merge and decrypt
    # decryptor.decrypt(unsplitter.unsplit_file('encrypted_file', 5), b'Password', 'test_image_2.png')
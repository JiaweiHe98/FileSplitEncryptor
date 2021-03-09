def split_file(cipherText, n: int):
    '''
    input a file and split it into n part
    '''

    #calculate the length for each item
    single_item_length = len(cipherText) // n

    #write them into different files
    for i in range(n):
        with open(f'encrypted_file.{i}', 'wb') as sf:
            if i == n - 1:
                sf.write(cipherText[single_item_length * i : ])
            else:
                sf.write(cipherText[single_item_length * i : single_item_length * (i + 1)])
        

if __name__ == "__main__":
    pass

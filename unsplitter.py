def unsplit_file(file_name: str, n: int):
    cipherText = b''
    for i in range(n):
        with open(file_name + '.' + str(i), 'rb') as item_file:
            item = item_file.read()
            cipherText += item

    return cipherText

if __name__ == "__main__":
    pass

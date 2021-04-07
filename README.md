# FileSplitEncryptor
A python program that can encrypt a file and split them into several segments with AES-256-CBC

## Prepare for Developing
This section will guide you through the software and tools required for building this project.

### Visual Studio Code
Visual Studio Code, also known as VSCode, is a popular and powerful text editor for developers. A good text editor is crucial for speeding up the coding process and debugging process.

#### Install Visual Studio Code
We recommend to use the official website for downloading the packages.
Please go to [https://code.visualstudio.com/](https://code.visualstudio.com/) and follow the instruction on the web page.

#### Recommended Extensions
We recommend you to install the listed extensions for boosting your coding experience with VSCode
* Python
* vscode-icons
* Code Spell Checker

### Python
Python is a widely used program language and both python2 and python3 interpreters are pre installed into Raspberry Pi OS and MacOS.

#### Install Python3 for Windows
Go to [https://www.python.org/downloads/](https://www.python.org/downloads/) and choose the version you prefer. Don't forget to add PATH for python interpreter.

#### Install pycryptodome package
pycryptodome is an evolution of pycrypto. pycryptodome can be installed through command line with pip. Type ```pip install pycryptodome``` to add pycryptodome library. Note that 

## Start Developing

### Advanced Encryption Standard (AES)
The Advanced Encryption Standard (AES), also known as Rijindael, is a widely use encryption standard for symmetric encryption, which uses the same key for both encrypting and decrypting. AES is also pretty fast since AES instruction set is now integrated into a large variety of processors, which provides hardware acceleration for the tasks associated with AES.

### AES Cipher Length
AES can only support several different key sizes, for example, 56 bits, 128 bits, 192 bits, and 256 bits. Higher the length is, higher the security level is, theoretically. Therefore, we need to pad or hash the key into one of the length that AES support.

### File Splitting and File Merging
Computers use binary to store files. An encrypted file is also stored in a computer's memory through a series of binary bits. So, if we cut the whole chunk of the file into pieces and remember the order of each piece, we will able to merge them on another machine without damaging the file.



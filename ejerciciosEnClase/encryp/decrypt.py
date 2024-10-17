from cryptography.fernet import Fernet
import os
os.system('cls')

with open('encryp/docSecret.docx', 'r') as llave:
    key = llave.read()

    fileDataDecrypt = "encryp/"
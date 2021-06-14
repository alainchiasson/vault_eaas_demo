#!/usr/bin/env python3
from cryptography.fernet import Fernet


def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def encrypt_message(message):
    """
    Encrypts a message
    """
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    
    with open("cipertext.txt", "wb") as cipher_file:
        cipher_file.write(encrypted_message)

if __name__ == "__main__":
    encrypt_message("encrypt this message")

#!/usr/bin/env python3
from cryptography.fernet import Fernet

import base64
import hvac
import os

client = hvac.Client(url=os.environ['VAULT_ADDR'],
                     token=os.environ['VAULT_TOKEN'])


def decrypt_key():
    
    ciphertext = open("cipher.key", "r").read()

    #encodedBytes= base64.b64encode(cc_number.encode("utf-8"))

    # encrypt_data_response = client.secrets.transit.encrypt_data(
    #     name = 'demo-key',
    #     plaintext = str(encodedBytes, "utf-8")
    # )

    # ciphertext = encrypt_data_response['data']['ciphertext']

    # print('Encrypted plaintext ciphertext is: {cipher}'.format(cipher=ciphertext))

    decrypt_data_response = client.secrets.transit.decrypt_data(
        name='demo-key',
        ciphertext=ciphertext,
    )

    plaintext = decrypt_data_response['data']['plaintext']
    
    with open("secret.key", "w") as key_file:
        key_file.write(decrypt_data_response['data']['plaintext'])

def generate_key():
    """
    Generates a key and save it into a file
    """
    gen_key_response = client.secrets.transit.generate_data_key(
        name='demo-key',
        key_type='plaintext',
    )

    with open("secret.key", "w") as key_file:
        key_file.write(gen_key_response['data']['plaintext'])
        
    with open("cipher.key", "w") as key_file:
        key_file.write(gen_key_response['data']['ciphertext'])


if __name__ == "__main__":
    decrypt_key()

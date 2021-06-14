#!/usr/bin/env python3
from cryptography.fernet import Fernet

import base64
import hvac
import os

client = hvac.Client(url=os.environ['VAULT_ADDR'],
                     token=os.environ['VAULT_TOKEN'])


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
    generate_key()

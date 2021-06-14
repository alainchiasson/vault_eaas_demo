#!/usr/bin/env python3
#
import base64
import hvac
import os

client = hvac.Client(url=os.environ['VAULT_ADDR'],
                     token=os.environ['VAULT_TOKEN'])

print ("Enter in your credit card number: ")
cc_number = input()

encodedBytes= base64.b64encode(cc_number.encode("utf-8"))

encrypt_data_response = client.secrets.transit.encrypt_data(
    name = 'demo-key',
    plaintext = str(encodedBytes, "utf-8")
)

ciphertext = encrypt_data_response['data']['ciphertext']

print('Encrypted plaintext ciphertext is: {cipher}'.format(cipher=ciphertext))

decrypt_data_response = client.secrets.transit.decrypt_data(
    name='demo-key',
    ciphertext=ciphertext,
)

plaintext = decrypt_data_response['data']['plaintext']
print('Decrypted plaintext is: {text}'.format(text=plaintext))
print('Base64 decoded plaintext is: {text}'\
    .format(text=str(base64.b64decode(plaintext), "utf-8")))


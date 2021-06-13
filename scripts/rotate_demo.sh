#!/usr/bin/env bash

# Rotate 
vault write -format json transit/encrypt/demo-key plaintext=$(base64 <<< "1111 1111 1111 1111") | jq -r '.data.ciphertext' > test1.txt

# decrypt
vault write -format json transit/decrypt/demo-key ciphertext=$(cat test1.txt) | jq -r '.data.plaintext' | base64 --decode

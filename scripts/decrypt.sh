#!/usr/bin/env bash

# decrypt
vault write -format json transit/decrypt/demo-key ciphertext=$(cat $1) | jq -r '.data.plaintext' | base64 --decode

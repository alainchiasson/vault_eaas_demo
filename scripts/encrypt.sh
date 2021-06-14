#!/usr/bin/env bash

# Encrypt 
vault write -format json transit/encrypt/demo-key plaintext=$(base64 <<< $( cat $1 )) | jq -r '.data.ciphertext'

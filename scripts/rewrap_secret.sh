#!/usr/bin/env bash

# Rotate
vault write -format json transit/rewrap/demo-key ciphertext=$(cat $1) | jq -r '.data.ciphertext'

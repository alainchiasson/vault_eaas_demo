#!/usr/bin/env bash
#
export VAULT_ADDR="http://vault-main:8200"

# Using a preset Vault Root Token 
vault login root

# Setup transit
vault secrets enable transit

vault write -f transit/keys/demo-key

vault read transit/keys/demo-key

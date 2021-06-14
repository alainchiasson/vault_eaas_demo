# Vault Encryption as A service Demo

This provides a quick qalk through for Vaults Encryption as a service. It helps demostrata a few concepts, notably:

The basics : 

- Creation of key spaces
- Encryption of data
- Decryption of data
- Key rotation
- Encrypted data rotation

Some aspects of general vault security :

- Limiting scope with policies
- Seperating personas

A vewi into incresing EaaS performance :

- Encrypting large datasets
- Horizontal scalling with performance clusters

This is meant to be self running / simple demostration. 

# Startup 

To start, launch docker compose. Our docker composes uses Hashicorps vault Enterprise container. Vault Ent has a limited licence use of 6 hours, which should be sufficient to properly demostrate everything. We also use the DEV versions with a fixed root key, as it makes the startup and setup easier. Currently we use root for all activities, but we seperate the personas. We expect this to translate well to the use proper roles for the applications and demonstrations.

# Setup 

Once started, we can run ```setup_vault.sh``` - this will create the encryption store and -eventually - the roles and profiles. 

# Base demo - bash

The ```base_demo.sh``` script demonstrates the basic feature of encryption and decryption using the vauklt-cli.

# rotate demo

note functional yet.

# Python Demos

These demostrate using other languages, and the programing interfaces. In this case python. 

## Base demo

The ```base-demo.py``` will encrypt and decrypt ( using the root key )

## Local encryption

The following demostrate a method to encrypt locally. The use case is for very large objects or for volumes where you would not want to generate the extra back and forth traffic.

It also demonstrates the ease at which it can be integrated into existing code. The scripts are :

```regular-genkey.py```  - it generates a local key using its own libraries.
```regular-encrypt.py``` - uses the generated key to encrypt.
```regular-decrypt.py``` - uses the generated key to decrypt.

The issue with the above scripts is the manipulation of the key - how to securly get the key from the encryption point to the decryption point.

Using vault we can generaate a datakey, that is itself encrypted. 

```vault-genkey.py``` - requests a datakey from vault, save the plaintext key and encrypted key.

Once generated we can use the same encrypt and decrypt code from above to do both actions. To solve the key transmission issue, we store the encrypted key with the encrypted data. At the decryption point, we can decrypt the included key and then decrypt the data. This is demostrated by the ```vault-genkey.py``` storing the encrypted key. FOr decryption we regenerate the plaintext key using :

```vault-decryptkey.py``` - decrypt the key ( instead of generating a new one )

NOTE: This might get confusing, as all the files are in the same directory - in production better structures would be used.

# Key rotation











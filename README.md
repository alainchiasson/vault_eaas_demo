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

To start, launch docker compose. Our docker composes uses both vault OSS and vault Ent. Vault Ent has a limited licence use of 6 hours, which should be sufficient to properly demostrate everything. We also use the DEV versions with a fixed root key, as it makes the startup and setup easier. Once setup, we will use proper roles for the applications and demonstrations.





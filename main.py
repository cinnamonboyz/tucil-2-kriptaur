from streamchipergpt import *

# Example usage
key = 'mysecretkey'.encode()  # Convert key to bytes
plaintext = 'Hello, world!'.encode()  # Convert plaintext to bytes

# Encryption
keystream = rc4(key)
ciphertext = bytearray()
for byte in plaintext:
    ciphertext.append(byte ^ next(keystream))
print(ciphertext.decode())

# Decryption
keystream = rc4(key)
decrypted = bytearray()
for byte in ciphertext:
    decrypted.append(byte ^ next(keystream))

print(decrypted.decode())  # Output: 'Hello, world!'
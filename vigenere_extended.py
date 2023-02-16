def extended_vigenere_encrypt(plain_text, key):
    key = key.upper()

    cipher = ''
    for i, plain_char in enumerate(plain_text):
        key_char = key[i % len(key)]
        cipher += chr((ord(plain_char) + ord(key_char)) % 256)
        
    return cipher

def extended_vigenere_decrypt(cipher_text, key):
    key = key.upper()

    plain = ''
    for i, cipher_char in enumerate(cipher_text):
        key_char = key[i % len(key)]
        plain += chr((ord(cipher_char) - ord(key_char)) % 256)
    return plain

if __name__ == "__main__":
    cipher = extended_vigenere_encrypt("rezaa", "abc")
    print(cipher)

    plain = extended_vigenere_decrypt("³§½¢£", "abc")
    print(plain)
    #print(plain)
    # with open("tucil 1/KTM.jpg", "rb") as save: 
    #     cipher = extended_vigenere_encrypt(save.read().decode("latin-1"), "KRIPTO")
    
    # with open("tucil 1/encrypted.jpg", 'wb') as save:
    #     save.write(cipher.encode('latin-1'))

    # with open("tucil 1/encrypted.jpg", "rb") as save:
    #     plain = extended_vigenere_decrypt(save.read().decode('latin-1'), "KRIPTO")

    # with open("tucil 1/decrypted.jpg", "wb") as save:
    #     save.write(plain.encode('latin-1'))
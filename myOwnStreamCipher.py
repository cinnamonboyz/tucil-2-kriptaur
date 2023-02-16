import playfair
import vigenere_extended

def swap(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
    return arr

def turnIntoASCII(text):
    return [ord(char) for char in text]

def ksa(key):
    s = [*range(256)]

    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) % 256
        swap(s, i, j)
    
    return s

def prga(s, text, vigenere_extended_cipher):
    i = 0
    j = 0
    c = []

    for idx in range(len(text)):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        swap(s, i, j)
        t = (s[i] + s[j]) % 256
        keystream = s[t]
        c.append(keystream ^ vigenere_extended_cipher[idx % len(vigenere_extended_cipher)] ^ text[idx])
    return bytearray(c)


def myOwnStreamCipher(text, key):
    vigenere_extended_cipher = turnIntoASCII(vigenere_extended.extended_vigenere_encrypt('REZA', key))

    text = turnIntoASCII(text)
    key = turnIntoASCII(key)

    s = ksa(key)
    result = prga(s, text, vigenere_extended_cipher)

    return result.decode('latin-1')

if __name__ == "__main__":
    cipher = myOwnStreamCipher("a", "asdf")
    print(cipher)
    
    plain = myOwnStreamCipher(cipher, "asdf")
    print(plain)

    # with open('foto.jpg', 'rb') as f:
    #     cipher = myOwnStreamCipher(f.read(), 'asdf')

    # with open('cipher_file.png', 'wb') as f:
    #     f.write(cipher)

    # with open('cipher_file.png', 'rb') as f:
    #     cipher = f.read()

    # with open('plain_file.png', 'wb') as f:
    #     f.write(myOwnStreamCipher(cipher, 'asdf'))
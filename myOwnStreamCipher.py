import base64

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

def prga(s, text):
    i = 0
    j = 0
    c = []

    for idx in range(len(text)):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        swap(s, i, j)
        t = (s[i] + s[j]) % 256
        keysteam = s[t]
        c.append(keysteam ^ text[idx])
    return bytearray(c)


def myOwnStreamCipher(text, key):
    if isinstance(text, str):
        text = turnIntoASCII(text)
    key = turnIntoASCII(key)

    s = ksa(key)
    result = prga(s, text)

    if isinstance(text, str):
        return result.decode('latin-1')
    else:
        return result

if __name__ == "__main__":
    # cipher = myOwnCipher("hallo guys2!", "asdf")
    # print(cipher)
    # print(base64.b64encode(cipher.encode('latin-1')))
    
    # plain = myOwnCipher(cipher, "asdf")
    # print(plain)

    with open('foto.jpg', 'rb') as f:
        cipher = myOwnStreamCipher(f.read(), 'asdf')

    with open('cipher_file.png', 'wb') as f:
        f.write(cipher)

    with open('cipher_file.png', 'rb') as f:
        cipher = f.read()

    with open('plain_file.png', 'wb') as f:
        f.write(myOwnStreamCipher(cipher, 'asdf'))

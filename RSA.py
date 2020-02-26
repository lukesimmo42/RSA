def create_public_key(p, q, e):
    return p*q, e


def create_private_key(p, q, e):
    return p*q, extended_euclidean(e, (p-1)*(q-1))


def extended_euclidean(a, b):
    storage = []

    while a != 0:
        storage.append(b // a)
        a, b = b % a, a

    x = 1
    y = - storage[len(storage) - 2]
    for i in range(len(storage) - 3, -1, -1):
        x, y = y, x + (y * - storage[i])

    return y


def encode(num, key):
    return num ** key[1] % key[0]


def cipher(text, public_key_):
    converted_text = [ord(c) for c in text]
    return [encode(i, public_key_) for i in converted_text]


def decipher(text, private_key_):
    converted_text = [encode(i, private_key_) for i in text]
    output = ""
    for c in converted_text:
        output += chr(c)
    return output


public_key = create_public_key(29, 37, 11)
private_key = create_private_key(29, 37, 11)
plain_text = \
    "Filler text is text that shares some characteristics of a real written text, but is random or otherwise generated."

print(cipher(plain_text, public_key))
print(decipher(cipher(plain_text, public_key), private_key))

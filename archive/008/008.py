# caeser-cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):

    encryptedText = ''

    for letter in text:
        if letter in alphabet:
            x = alphabet.index(letter)
            y = x + shift
            encryptedText += alphabet[y]
        else:
            print('wrong ip')

    print(f"The encrypted text is {encryptedText}")


def decrypt(text, shift):

    decryptedText = ''

    for letter in text:
        if letter in alphabet:
            x = alphabet.index(letter)
            y = x - shift
            decryptedText += alphabet[y]
        else:
            print('wrong ip')

    print(f"The decoded text is {decryptedText}")


decrypt("cd", 2)

if direction == 'encode':
    encrypt('5', 1)
elif direction == 'decode':
    decrypt("bcd", 1)
else:
    print('check direction')

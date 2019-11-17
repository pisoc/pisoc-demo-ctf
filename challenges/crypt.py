#!/usr/bin/python3.6

import codecs
import base64
import sys


def rot13(text):
    """For an explanation: https://en.wikipedia.org/wiki/ROT13#Description"""
    return codecs.getencoder("rot-13")(text)[0]


def handle_encrypt_mode(cleartext):
    """Super secret encryption algorithm"""
    # Apply rot13
    ciphertext = rot13(cleartext)

    # Reverse the ciphertext
    ciphertext = ciphertext[::-1]

    # Encode with base64
    ciphertext = base64.b64encode(ciphertext.encode()).decode()

    # Display the encrypted data
    print(ciphertext)


def handle_decrypt_mode(ciphertext):
    # Code has been removed
    pass


if __name__ == '__main__':
    # Ensure we have 3 arguments and the 2nd is 'enc' or 'dec'
    if (len(sys.argv) != 3) or (sys.argv[1] not in ('enc', 'dec')):
        file = sys.argv[0]
        print(f'Usage:\n{file} enc <cleartext>\n{file} dec <ciphertext>')
        sys.exit(1)

    # Decide between encrypt and decrypt
    if sys.argv[1] == 'enc':
        handle_encrypt_mode(sys.argv[2])
    elif sys.argv[1] == 'dec':
        handle_decrypt_mode(sys.argv[2])

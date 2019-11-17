#!/usr/bin/python3.6

import codecs

def apply_rot13(text):
    # For an explanation:
    # https://en.wikipedia.org/wiki/ROT13#Description
    return  codecs.getencoder("rot-13")(text)[0]

def handle_encrypt_mode():
    # Get cleartext password from the user
    cleartext = input('Password: ')

    # Apply top-secret rot13 encryption algorithm
    ciphertext = apply_rot13(cleartext)

    # Add an extra layer of security
    ciphertext = ciphertext[::-1]

    # Display the encrypted password
    print(ciphertext)

def handle_decrypt_mode():
    # Code has been removed  
    pass


if __name__ == '__main__':
    # Decide between encrypt and decrypt
    mode = input('Mode [enc|dec]: ')

    if mode == 'enc':
        handle_encrypt_mode()
    elif mode == 'dec':
        handle_decrypt_mode()
    else:
        print('Please input either "enc" or "dec" - you entered {mode}')

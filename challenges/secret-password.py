#!/usr/bin/python3.6


# Encrypt and decrypt passwords
# Decrypt logic is missing
# What's the password stored in the password.txt file, or this file?


# def encrypt_password():
#     pass


# def decrypt_password():
#     pass


def handle_encrypt_mode():
    cleartext = input('Password: ')

    # Switch to upper case
    ciphertext = cleartext.upper()

    # Reverse the string
    ciphertext = ciphertext[::-1]

    print(ciphertext)


def handle_decrypt_mode():
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

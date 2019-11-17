#!/usr/bin/python3.6
import sqlite3
import hashlib
import string
import itertools


def sha256(message):
    """Calculate the sha256 hash of a given string"""
    return hashlib.sha256(message.encode()).hexdigest()


def load_password():
    """Load password from password.db sqlite3 database"""
    con = sqlite3.connect('passwords.db')
    cur = con.cursor()
    cur.execute('SELECT password FROM users WHERE username = "admin"')
    pw_hash = cur.fetchone()[0]
    con.commit()
    con.close()
    return pw_hash


def bruteforce(target_hash):
    """Generate strings and test them against a password hash"""
    alphabet = string.ascii_lowercase
    length = 1

    while 1:
        print(f'[+] Trying length = {length}')
        for item in itertools.product(alphabet, repeat=length):
            attempt = "".join(item)
            attempt_hash = sha256(attempt)

            if target_hash == attempt_hash:
                return attempt
        length += 1


if __name__ == '__main__':
    print('[+] Starting bruteforce attack')
    password = bruteforce(load_password())

    print(f'[!] Cracked!')
    print(f'[!] Hash: {sha256(password)}')
    print(f'[!] Password: {password}')

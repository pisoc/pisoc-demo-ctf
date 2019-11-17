#!/usr/bin/python3.6
"""Create password.db and insert credentials admin::sha256(<password>)"""

import sqlite3
import hashlib
import sys

if __name__ == '__main__':
    # We need a password argument to be able to run
    if len(sys.argv) != 2:
        print(f'Usage:\n{sys.argv[0]} <password>')
        sys.exit(1)

    # Get SHA256 hash of password
    digest = hashlib.sha256(sys.argv[1].encode()).hexdigest()

    # Insert hashed password into DB
    con = sqlite3.connect('passwords.db')
    cur = con.cursor()

    # Ensure only one entry exists in the DB
    cur.execute('DROP TABLE IF EXISTS users')
    cur.execute('CREATE TABLE IF NOT EXISTS users (username, password)')

    cur.execute('INSERT INTO users values (?, ?)', ('admin', digest))

    con.commit()
    con.close()

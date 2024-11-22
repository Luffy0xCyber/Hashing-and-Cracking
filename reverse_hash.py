#!/usr/bin/env python3

"""
Password search script based on a hash.

It takes a hash and a dictionary file as input, then the script will try to find a password in the dictionary that matches the given hash.

It supports => MD5, SHA1, SHA224, SHA256 hashes!

NOTE: I limited myself to these types of hashes, there was a possibility to add others, but I was afraid it would be long and maybe less efficient.

Usage:
./reverse_hash.py <hash> <dictionary_file>

Example:

./reverse_hash.py b97819074f88f63734e081ce70e0778b passwords.lst


Warning: Do not forget to give execution permissions to the file!
"""


import sys
import hashlib


def hash_password(password):
    """
    Hashes the password using MD5, SHA1, SHA224 and SHA256.
    :param password: The password to hash.
    :type password: str
    :return: A dictionary containing the hashes of the password for each algo.
    """
    encoding = password.encode()
    return {
        "MD5": hashlib.md5(encoding).hexdigest(),
        "SHA1": hashlib.sha1(encoding).hexdigest(),
        "SHA224": hashlib.sha224(encoding).hexdigest(),
        "SHA256": hashlib.sha256(encoding).hexdigest()
    }


def inverse_hash(hash_target, dictionary):
    """
    Tries to find a password in the dictionary that matches the hash target.
    :param hash_target: The hash to search for.
    :type hash_target: str
    :param dictionary: The path to the dictionary file.
    :type dictionary: str
    :return: A tuple containing the found password (or None) and the hash type (or None).

    """
    with open(dictionary, 'r', encoding="utf-8") as file:
        for line in file:
            password = line.strip()
            hashes = hash_password(password)
            
            for type_hash, hash_value in hashes.items():
                if hash_target == hash_value:
                    return password, type_hash
    
    return None, None

def main():
    if len(sys.argv) != 3:
        print("Usage: ./reverse_hash.py <hash> <dictionary>")
        sys.exit(1)

    hash_target = sys.argv[1]
    dictionary = sys.argv[2]

    password, type_hash = inverse_hash(hash_target, dictionary)

    if password:
        print(f"Found password `{password}` with matching {type_hash} hash.")
    else:
        print("No matching password found in given dictionary.")

if __name__ == "__main__":
    main()
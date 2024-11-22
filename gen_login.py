#!/usr/bin/env python3
#
# `gen_login.py username password` will generate a password entry of the form
# `username:bcrypt_hash` on the standard output.

import sys
import bcrypt


def generate_login_entry(user_name, mdp):
    """
    Generates a login entry of the form "username:bcrypt_hash".
    :param user_name: The username.
    :type user_name: str
    :param mdp: The password in clear.
    :type mdp: str
    :return: A string in the format "username:bcrypt_hash\n".
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(mdp.encode('utf-8'), salt)

    return f"{user_name}:{hashed.decode('utf-8')}\n"


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} username password", file=sys.stderr)
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    # Build login entry and print it
    login_entry = generate_login_entry(username, password)
    print(login_entry)
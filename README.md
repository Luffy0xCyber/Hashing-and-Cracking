
# Password Hashing and Cracking Scripts

[![Build Status](https://cdn.prod.website-files.com/5e0f1144930a8bc8aace526c/65dd9eb5aaca434fac4f1c7c_Build-Passing-brightgreen.svg)](https://github.com/Luffy0xCyber/Hashing-and-Cracking/actions)
[![License](https://img.shields.io/badge/License-Unlicensed-blue.svg)](https://github.com/Luffy0xCyber/Hashing-and-Cracking/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![GitHub last commit](https://img.shields.io/github/last-commit/Luffy0xCyber/Hashing-and-Cracking)]()

This repository contains two Python scripts designed for password security and analysis:
1. **`gen_login.py`**: A script for generating secure bcrypt-based hashed passwords.
2. **`reverse_hash.py`**: A script for cracking hashed passwords using a dictionary-based approach.

Both scripts are inspired by the tools and concepts described on [Crackstation.net](https://crackstation.net/), and follow their recommendations for proper password hashing and cracking techniques.

---

## Features

### `gen_login.py`
- Generates a secure bcrypt hash for a username-password pair.
- Outputs the result in the format: `username:bcrypt_hash`.
- Designed to safeguard user credentials against brute force and dictionary attacks.

### `reverse_hash.py`
- Attempts to crack a given hash using a provided dictionary file.
- Supports multiple hashing algorithms:
  - _MD5_
  - _SHA1_
  - _SHA224_
  - _SHA256_
- Outputs the discovered password or indicates that no match was found.

---

## Requirements

### Prerequisites
- Python 3.7 or later.
- [bcrypt](https://pypi.org/project/bcrypt/) Python library (for `gen_login.py`).

Install dependencies:
```bash
pip install bcrypt
```

### Supported Platforms
- **Windows**
- **Linux**
- **macOS**

---

## Installation

### Windows
1. **Install Python**:
   - Download the latest version of Python from [python.org](https://www.python.org/).

2. **Clone the repository**:
   ```bash
   git clone https://github.com/Luffy0xCyber/Hashing-and-Cracking.git
   cd Hashing-and-Cracking
   ```

3. **Install dependencies**:
   ```bash
   pip install bcrypt
   ```

4. **Run the scripts**:
   - To generate a hashed password:
     ```bash
     python gen_login.py <username> <password>
     ```
   - To crack a hash:
     ```bash
     python reverse_hash.py <hash> <dictionary_file>
     ```

### Linux & macOS
1. **Install Python**:
   - Most Linux and macOS systems have Python pre-installed. To install or update Python refers to [How to install Python on Linux?](https://www.geeksforgeeks.org/how-to-install-python-on-linux/)

2. **Clone the repository**:
   ```bash
   git clone https://github.com/Luffy0xCyber/Hashing-and-Cracking.git
   cd Hashing-and-Cracking
   ```

3. **Install dependencies**:
   ```bash
   pip3 install bcrypt
   ```

4. **Run the scripts**:
   - Make the scripts executable:
     ```bash
     chmod +x gen_login.py reverse_hash.py
     ```
   - To generate a hashed password:
     ```bash
     ./gen_login.py <username> <password>
     ```
   - To crack a hash:
     ```bash
     ./reverse_hash.py <hash> <dictionary_file>
     ```

---

## Usage Examples

### Generating a Secure Login Entry
```bash
python gen_login.py alice mysecurepassword
```
Output:
```plaintext
alice:$2b$12$H3wGJ6fjBZ9Mhfji.FqauuLHo0QxQj2blfQQDXMifJ5FA9XEzpX2m
```

### Cracking a Hash
Given a hash `5f4dcc3b5aa765d61d8327deb882cf99` and a dictionary file `passwords.lst` :
```bash
python reverse_hash.py 5f4dcc3b5aa765d61d8327deb882cf99 passwords.lst
```
**_About the dictionary file, you can create a list of passwords or download it from the internet. For example, you can download a list of passwords from [here](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt)**_

Output:
```plaintext
Found password `password` with matching MD5 hash.
```

---

## Security Practices

This repository is inspired by [Crackstation](https://crackstation.net/), a well-known resource for password security. The recommendations for secure password storage, such as using bcrypt with proper salt, are implemented in `gen_login.py`. For more information on securing passwords, refer to [this article](https://crackstation.net/hashing-security.htm#properhashing).

---

## Limitations
- `reverse_hash.py` is limited to MD5, SHA1, SHA224, and SHA256 algorithms.
- Cracking efficiency depends on the size and quality of the dictionary file.

---

## License

This project is no licensed. You are free to use, modify, and distribute the code as needed.

---

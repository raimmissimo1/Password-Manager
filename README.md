# Password-Manager
Password Manager always ready to help you

🧩 Description

This project is a simple password manager written in Python that uses the Fernet symmetric encryption system from the cryptography library.
It allows users to securely store, view, and manage passwords, all saved in an encrypted form in a text file (passwords.txt).

A separate encryption key (key.key) is generated once and used to encrypt and decrypt all stored passwords.
This makes the data unreadable without the correct key, ensuring privacy and security.

⚙️ How It Works

When the program starts, it checks for the existence of an encryption key file:

If it doesn’t exist, a new key is automatically created and saved in key.key.

If it exists, the key is loaded for encryption/decryption.

The user enters a master password (used as access control).

The program presents a simple text-based menu:

1. View passwords → Decrypts and displays all stored passwords.

2. Add a password → Encrypts a new password and saves it to the file.

3. Exit → Ends the program

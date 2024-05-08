from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

def pad(data):
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    return padded_data

def unpad(data):
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_data = unpadder.update(data) + unpadder.finalize()
    return unpadded_data

def encrypt(key, plaintext):
    iv = os.urandom(16)  # Generate a random IV (Initialization Vector)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_plaintext = pad(plaintext)
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    return iv + ciphertext

def decrypt(key, ciphertext):
    iv = ciphertext[:16]  # Extract the IV from the ciphertext
    ciphertext = ciphertext[16:]  # Extract the actual ciphertext
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    return unpad(decrypted_data)

# Example usage
password = b"super_secret_password"
plaintext = b"Hello, AES encryption!"

# Derive a key from the password using PBKDF2
salt = os.urandom(16)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = kdf.derive(password)

# Encryption
ciphertext = encrypt(key, plaintext)
print("Encrypted:", ciphertext)

# Decryption
decrypted_text = decrypt(key, ciphertext)
print("Decrypted:", decrypted_text.decode('utf-8'))

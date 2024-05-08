from pyDes import des, PAD_PKCS5
import binascii

def encrypt(key, data):
    cipher = des(key, PAD_PKCS5)
    # Ensure data length is a multiple of 8 bytes by padding
    padded_data = data + (8 - len(data) % 8) * b'\0'
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data

def decrypt(key, encrypted_data):
    cipher = des(key, PAD_PKCS5)
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data


key = b"abcdefgh"  # 8-byte key
plaintext = b"Hello MY NAME IS Abid, DES encryption!"

# Encryption
encrypted_data = encrypt(key, plaintext)
print("Encrypted:", binascii.hexlify(encrypted_data))

# Decryption
decrypted_data = decrypt(key, encrypted_data)
print("Decrypted:", decrypted_data.decode('utf-8'))

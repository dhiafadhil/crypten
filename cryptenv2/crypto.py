from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


def encrypt(data):
    with open('public_key.pem', 'rb') as f:
        key = RSA.importKey(f.read())
    cipher = PKCS1_OAEP.new(key)
    encrypted = cipher.encrypt(data)
    return base64.b64encode(encrypted).decode("utf-8")


def decrypt(data):
    with open('private_key.pem', 'rb') as f:
        key = RSA.importKey(f.read())
    cipher = PKCS1_OAEP.new(key)
    decrypted = cipher.decrypt(base64.b64decode(data))
    return decrypted



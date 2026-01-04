import socket
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

KEY = b'Sixteen byte key'
IV = get_random_bytes(16)

def encrypt_message(message):
    data = message.encode()
    padding_len = 16 - (len(data) % 16)
    data += bytes([padding_len]) * padding_len

    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    encrypted = cipher.encrypt(data)
    return base64.b64encode(IV + encrypted)

print("🔹 Client started")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5000))
print("🔹 Connected to server")

encrypted_msg = encrypt_message("Hello Secure World")
client_socket.send(encrypted_msg)
print("🔹 Encrypted message sent")

client_socket.close()
print("🔹 Client closed connection")

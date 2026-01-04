import socket
from Crypto.Cipher import AES
import base64

KEY = b'Sixteen byte key'

def decrypt_message(encrypted_message):
    raw = base64.b64decode(encrypted_message)

    iv = raw[:16]
    ciphertext = raw[16:]

    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(ciphertext)

    padding_len = decrypted_data[-1]
    return decrypted_data[:-padding_len].decode()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5000))
server_socket.listen(1)

print(" Server listening on port 5000...")

conn, addr = server_socket.accept()
print("Connected by", addr)

data = conn.recv(2048)
print("Encrypted received:", data.decode())

plaintext = decrypt_message(data.decode())
print("Decrypted message:", plaintext)

conn.close()
server_socket.close()

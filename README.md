#  AES Secure Client–Server Communication (Python)

A simple yet **industry-aligned cryptography + networking project** demonstrating **AES-128 (CBC mode)** encrypted communication between a Python client and server using TCP sockets.

This project is suitable for:

* Cyber Security / SOC portfolios
* Cryptography fundamentals
* Networking & secure communication demos

---

##  Features

* AES-128 encryption (CBC mode)
* Secure random IV generation
* Base64 encoding for safe transport
* Client → Server encrypted message
* Server → Client encrypted reply
* Proper PKCS7 padding & removal
* Python 3.10+ compatible (tested on Python 3.13, Windows)

---

##  Project Structure

```
AES-Secure-Client-Server/
│
├── AES_server.py      # Secure AES-enabled TCP server
├── AES_CLIENT.py      # Secure AES-enabled TCP client
├── README.md          # Project documentation
└── .gitignore         # (optional)
```

---

## ⚙️ Prerequisites

* Python **3.10 or higher**
* pip (Python package manager)

### Required Library

```bash
pip install pycryptodome
```

> ⚠️ Do NOT install `crypto` — use **pycryptodome** only.

---

##  How It Works (High-Level Flow)

1. Client encrypts a message using AES-128-CBC
2. Client sends encrypted data + IV to server
3. Server decrypts and reads client message
4. Server encrypts its own reply
5. Client decrypts and prints server reply

All data sent over the socket is **encrypted**.

---

## ▶️ How to Run the Project

### 1️⃣ Start the Server (Terminal 1)

```bash
cd path/to/project
python AES_server.py
```

Expected output:

```
Server listening on port 5000...
```

---

### 2️⃣ Run the Client (Terminal 2)

```bash
cd path/to/project
python AES_CLIENT.py
```

Expected output:

```
Client started
Connected to server
Encrypted message sent
Decrypted reply: Hello Client, message received securely
```

---

##  Cryptography Details

| Component | Value             |
| --------- | ----------------- |
| Algorithm | AES               |
| Key Size  | 128-bit           |
| Mode      | CBC               |
| IV        | Random (16 bytes) |
| Padding   | PKCS7             |
| Transport | TCP Socket        |

>  **Note:** AES-CBC is used here for learning. In production, prefer **AES-GCM**.

---

## 📂 Example Messages

**Client → Server (Encrypted):**

```
Hello Secure World
```

**Server → Client (Encrypted Reply):**

```
Hello Client, message received securely
```

---

##  Why This Project Matters

This project demonstrates:

* Practical cryptography usage
* Secure socket programming
* Encryption + decryption lifecycle
* Real-world client–server communication

---

##  Security Notes

* Keys are hardcoded **only for demonstration**
* IV is generated securely using `get_random_bytes`
* No plaintext is transmitted over the network

🚨 **Do NOT hardcode keys in real applications**

---

## 🛠️ Future Improvements

* [ ] Upgrade to AES-GCM (Authenticated Encryption)
* [ ] Secure key exchange (Diffie–Hellman)
* [ ] Multi-client support
* [ ] Logging & intrusion detection hooks
* [ ] TLS-based communication

---

## 👤 Author

**Raj**
Computer Science Engineering Student
Cybersecurity & Networking Enthusiast

---



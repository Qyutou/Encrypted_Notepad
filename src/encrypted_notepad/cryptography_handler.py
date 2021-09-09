import hashlib
from Crypto.Cipher import AES
from tkinter.simpledialog import askstring


def get_hashed_password(password):
    return hashlib.md5(password.encode("utf-8")).digest()


def encode_text(text, file_out_name):
    password = askstring("Password", "Enter password:", show='*')
    key_16bytes = get_hashed_password(password)
    message = bytes(text, encoding="utf-8")

    cipher = AES.new(key_16bytes, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message)

    file_out = open(file_out_name, "wb")
    [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
    file_out.close()


def decode_text(file_in_name):
    file_in = open(file_in_name, "rb")
    nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]

    password = askstring("Password", "Enter password:", show='*')
    key_16bytes = get_hashed_password(password)
    cipher = AES.new(key_16bytes, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    return data

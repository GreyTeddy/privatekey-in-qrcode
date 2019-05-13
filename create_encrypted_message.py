from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def get_public_key():
    with open("public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
        print("-Public key received")
        return public_key

def encrypt_message(public_key):
    message = input("Enter message to be encrypted: ").encode('UTF-8')
    encrypted = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("-Encrypted message created")
    return encrypted

def create_encrypted_message_file(encrypted):
    with open('encrypted_message.txt', 'wb') as f:
        f.write(encrypted)
        print(encrypted)
        print("-Encrypted message saved in encrypted_message.txt")

if __name__ == "__main__":
    create_encrypted_message_file(encrypt_message(get_public_key()))
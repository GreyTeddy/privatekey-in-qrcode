from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from pyqrcode import QRCode

# create private and public key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=512,
    backend=default_backend()
)
print("-Created private key")
public_key = private_key.public_key()
print("-Created public key")

# stringify the private and public key
pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
print("-Stringified public key")
pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print("-Stringified public key")

#create public key file
with open('public_key.pem', 'wb') as f:
    f.write(pem_public)
print("-Created public key file")

#create private key svg
qr = QRCode(pem_private)
qr.svg("private_key.svg", scale=3)
print("-Created private key svg")

print("-Done")
from pyqrcode import QRCode
import cv2
import pyzbar.pyzbar as pyzbar
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# create and store private key to qr code svg

# create private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=512,
    backend=default_backend()
)

# stringify the private key

pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

pem_private = pem_private
print(pem_private)

qr = QRCode(pem_private)
qr.svg("private_key.svg", scale=3)

################################################

#check created qr code

#read qr code
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame = cap.read()
    try:
        # display text
        got_text = pyzbar.decode(frame)[0].data
        cv2.putText(frame, "Detected", (0, 50), font, 1,(255,255,255), 3)
        #check if correct qr code
        if got_text == pem_private:
            print(True)
    except:
        pass
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    # if esc is pressed
    if key == 27:
        break

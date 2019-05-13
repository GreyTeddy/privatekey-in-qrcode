import cv2
import pyzbar.pyzbar as pyzbar
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

#read qr code (private key)
def read_qr():
    cap = cv2.VideoCapture(0)
    # run the camera
    while True:
        _, frame = cap.read()
        try:
            # display text
            got_text = pyzbar.decode(frame)[0].data
            print("-QRCode Detected")
            return got_text
        except:
            pass
        cv2.imshow("Frame", frame)

        # wait for esc to be pressed
        key = cv2.waitKey(1)
        if key == 27:
            print("Exited")
            exit()


def get_encrypted_message():
    with open("encrypted_message.txt", "rb") as key_file:
        encrypted_message = key_file.read()
        print("-Encrypted message read")
        return encrypted_message

def decrypt_message(pem_private,encrypted_message):
    #deserialise key
    private_key = serialization.load_pem_private_key(
        pem_private,
        password=None,
        backend=default_backend()
    )
    #decrypt the message
    decrypted = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("-Message decrypted")
    print("Message: {}".format(decrypted.decode("utf-8")))
    #create decrypted_message.txt
    with open('decrypted_message.txt', 'wb') as f:
        f.write(decrypted)
        print(decrypted)
        print("-Decrypted message saved in decrypted_message.txt")


if __name__ == "__main__":
    decrypt_message(read_qr(),get_encrypted_message())
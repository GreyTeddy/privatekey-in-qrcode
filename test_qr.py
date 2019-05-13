from pyqrcode import QRCode
import cv2
import pyzbar.pyzbar as pyzbar

def create_qr_code(text=False):
    if(text):
        qr = QRCode(input("Enter qr code text: "))
    else:
        qr = QRCode(input("Hello World"))
    qr.svg("private_key.svg", scale=6)

def read_qr_code():
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_PLAIN

    while True:
        _, frame = cap.read()

        decodedObjects = pyzbar.decode(frame)
        print(decodedObjects)
        for obj in decodedObjects:
            cv2.putText(frame, str(obj.data), (0, 50), font, 2,
                        (255, 0, 0), 3)

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        # if esc is pressed
        if key == 27:
            break

if __name__ == "__main__":
    while True:
        hello = input("(c)reate, (r)ead or (e)xit: ")
        if hello=="c":
            create_qr_code(True)
        elif hello=="r":
            read_qr_code()
        elif hello=="e":
            break

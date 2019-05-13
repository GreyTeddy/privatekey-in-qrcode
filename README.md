# Public Key encryption using QR Codes

Is this dumb? Is this smart? Maybe both cause the camera's resolution might be meh...

This program asks you to show a QR code containing the private key in order to get a message.

You can also create the public/private key pair (don't worry the public key is a file).


## Installation
### Python
1. Install python 3.x (any version of python3 should work)

### ZBar
2. Download [ZBar](http://zbar.sourceforge.net/download.html) and Install

### Download the files
3. Download the source files 

### pip
4. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all requirements.
  ```bash
  pip install -r requirements.txt
  ```
### Run files
5. Run 
      - create_bundle.py
          
          This will create the files:
          - public_key.pem
          - private_key.svg
      - create_encrypted_text.py 
      
          Will ask for:
          - message to be encrypted
          
          Will create the file:
          - encrypted_text.txt
      - create_decrypted_text.py
      
          Will ask for:
          - QRCode to be shown on webcam
          
          Will create the file:
          - encrypted_text.txt

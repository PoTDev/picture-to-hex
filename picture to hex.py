import sys
import binascii

# file = "\\\\.\\E:"
file = "picture.jpg"
with open(file, 'rb') as f:
    print("Disk Open")
    data = f.read()
    # Convert the binary data to upper case hex ascii code
    # hex_data = " ".join("{:02X}".format(c) for c in data)
    sys.stdout = open("test.txt", "w")
    print(binascii.hexlify(data))

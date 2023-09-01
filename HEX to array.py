file = "picture.jpg"
with open(file, 'rb') as f:
    print("Disk Open")
    data = f.read(16)  # массив из 8битных чисел
    for c in data:
        print(c)
    hex_data = " ".join("{:02X}".format(c) for c in data)
    print(hex_data)
    arr = hex_data.split()
    print(arr)

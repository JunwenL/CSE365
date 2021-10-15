rotate = 1
for c in range(65,122):
    xord = 0xa1 ^ c
    rotated = (xord >> rotate) | (xord << 8 - rotate) & 0xff
    print(chr(c), end = " ")
    print(hex(rotated))
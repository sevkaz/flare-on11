def GenerateFlagText(x, y):
    key = x + y * 20
    encoded = "\xa5\xb7\xbe\xb1\xbd\xbf\xb7\x8d\xa6\xbd\x8d\xe3\xe3\x92\xb4\xbe\xb3\xa0\xb7\xff\xbd\xbc\xfc\xb1\xbd\xbf"
    return ''.join([chr(ord(c) ^ key) for c in encoded])

# Kurbağa hedef noktasına (10, 10) ulaştığında bayrağı hesapla
x = 10
y = 10
flag = GenerateFlagText(x, y)
print(flag)

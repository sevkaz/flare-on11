import base64

# Base64 encoded string
base64_encoded = "base64_decoded_string"

# XOR key
xor_key = "key"

# Step 1: Decode the base64 string
decoded_bytes = base64.b64decode(base64_encoded)

# Step 2: XOR the decoded bytes with the key
def xor_decrypt(data, key):
    key_bytes = key.encode('utf-8')
    decrypted_bytes = bytearray()

    for i in range(len(data)):
        decrypted_bytes.append(data[i] ^ key_bytes[i % len(key_bytes)])

    return bytes(decrypted_bytes)

# Decrypt the decoded bytes using XOR with the key
decrypted_data = xor_decrypt(decoded_bytes, xor_key)

# Step 3: Print the decrypted result (usually as a string)
print("Decrypted result:", decrypted_data.decode('utf-8', errors='ignore'))

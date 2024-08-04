# Function to decrypt the JSON file
def decrypt_file():
    key = load_key()
    fernet = Fernet(key)
    
    with open(r'D:\python\iot blockchain\data.json', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    
    decrypted = fernet.decrypt(encrypted)
    
    with open(r'D:\python\iot blockchain\data.json', 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

# Decrypt the JSON file
decrypt_file()

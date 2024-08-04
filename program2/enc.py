# Function to generate and save an encryption key
def generate_key():
    key = Fernet.generate_key()
    with open(r'D:\python\iot blockchain\encryption.key', 'wb') as key_file:
        key_file.write(key)
    return key

# Function to load the encryption key from file
def load_key():
    return open(r'D:\python\iot blockchain\encryption.key', 'rb').read()

# Function to encrypt the JSON file
def encrypt_file():
    key = load_key()
    fernet = Fernet(key)
    
    with open(r'D:\python\iot blockchain\data.json', 'rb') as file:
        original = file.read()
    
    encrypted = fernet.encrypt(original)
    
    with open(r'D:\python\iot blockchain\data.json', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


# Generate and save the encryption key
generate_key()

# Encrypt the JSON file
encrypt_file()

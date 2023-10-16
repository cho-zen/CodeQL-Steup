import hashlib

# Insecure Authentication
def insecure_authentication(password, stored_password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password == stored_password

# Password storage (insecure)
stored_password = "5d41402abc4b2a76b9719d911017c592"  # Hash of "password123"

# User input
user_password = input("Enter your password: ")

if insecure_authentication(user_password, stored_password):
    print("Authentication successful!")
else:
    print("Authentication failed!")

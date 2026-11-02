
# ==========================================
# ASSIGNMENT 2: XOR ENCRYPTION AND DECRYPTION
# ==========================================

# STEP 1: Take message input from user

message = input("Enter your message: ")

# The user enters the text that needs to be encrypted.


# STEP 2: Define secret encryption key

key = 5

# A secret key is used to perform the XOR operation.
# The SAME key is required for both encryption and decryption.


# STEP 3: Create an empty string for encrypted data

encrypted = ""

# This string will store the encrypted message.


# STEP 4: Encrypt the message using XOR

for ch in message:

    # ord(ch) converts character into its integer (ASCII/Unicode) value
    # ^ performs XOR operation with the secret key
    # chr() converts the result back into a character

    encrypted += chr(ord(ch) ^ key)

# Each character is encrypted separately using XOR.
# The encrypted characters are added to the encrypted string.


# Display encrypted message

print("Encrypted Message:", encrypted)


# STEP 5: Create an empty string for decrypted data

decrypted = ""

# This string will store the original message after decryption.


# STEP 6: Decrypt using the SAME XOR key

for ch in encrypted:

    # XOR the encrypted character with the same key again.
    # This recovers the original character because:
    # (A XOR B) XOR B = A

    decrypted += chr(ord(ch) ^ key)


# STEP 7: Display decrypted message

print("Decrypted Message:", decrypted)

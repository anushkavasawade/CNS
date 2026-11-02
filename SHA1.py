
# ==========================================
# ASSIGNMENT 4: SHA-1 MESSAGE DIGEST
# AND AVALANCHE EFFECT
# ==========================================

# STEP 1: Import hashing library

import hashlib

# hashlib is a built-in Python library.
# It provides different hashing algorithms like SHA-1,
# SHA-256, SHA-512, etc.


# STEP 2: Take message input

message = input("Enter a message: ")

# The user enters the original message.
# This message will be converted into a hash value.


# STEP 3: Generate SHA-1 hash of original message

# encode() converts string into bytes
# sha1() generates the hash
# hexdigest() converts hash into hexadecimal format

hash_value = hashlib.sha1(message.encode()).hexdigest()

# SHA-1 generates a fixed-length hash of 160 bits.
# The hexadecimal representation contains 40 characters.


# STEP 4: Display original message and hash

print("\nOriginal Message:", message)
print("SHA-1 Hash:", hash_value)

# Display the original message and its SHA-1 digest.


# STEP 5: Modify the original message

# Add one character to the original message

modified_message = message + "A"

# We add the character A to change the original message.
# Even a small change in the input should produce
# a significantly different hash value.


# STEP 6: Generate hash of modified message

modified_hash = hashlib.sha1(
    modified_message.encode()
).hexdigest()

# Generate the SHA-1 hash of the modified message.
# It uses the same hashing algorithm as before.


# STEP 7: Display modified message and hash

print("\nModified Message:", modified_message)
print("Modified Hash:", modified_hash)

# Display the modified message and its hash value.


# STEP 8: Compare both hash values

if hash_value != modified_hash:

    print("\nMessage has been modified!")
    print("Avalanche Effect Demonstrated!")

else:

    print("\nHashes are identical.")

# If both hashes are different, the input messages
# have produced different hash values.
# This demonstrates the avalanche effect.



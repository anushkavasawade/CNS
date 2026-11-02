
# ==========================================
# ASSIGNMENT 7: DIGITAL SIGNATURE USING DSS
# ==========================================

# STEP 1: Import required libraries

from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

# dsa: Used to generate DSA private and public keys.
# hashes: Used for SHA-256 hashing.
# InvalidSignature: Handles invalid digital signatures.


# STEP 2: Generate DSA private key

private_key = dsa.generate_private_key(key_size=2048)

# Generate a private key of 2048 bits.
# The private key is secret and belongs to the vendor.
# It is used to generate the digital signature.


# STEP 3: Generate public key from private key

public_key = private_key.public_key()

# Extract the public key from the private key.
# The public key is shared with the receiver.
# It is used to verify the digital signature.


# STEP 4: Accept message from user

# encode() converts string into bytes

message = input("Enter message: ").encode()

# The vendor enters the tender document or message.
# The message is converted into bytes before signing.


# STEP 5: Generate digital signature using private key

# SHA256 is used to generate the message digest

signature = private_key.sign(message, hashes.SHA256())

# SHA-256 generates a hash of the message.
# DSA uses the private key and message digest
# to generate a digital signature.
# The signature is unique to the message and private key.


# STEP 6: Display generated digital signature

print("Digital Signature Generated!")

print("Signature:", signature.hex())

# Display the generated digital signature.
# hex() converts the signature bytes into hexadecimal format.


# STEP 7: Verify digital signature using public key

try:

    public_key.verify(signature, message, hashes.SHA256())

    print("Signature is Valid!")

# The receiver uses the public key to verify the signature.
# If the signature matches the message, verification succeeds.


# STEP 8: Handle invalid signature

except InvalidSignature:

    print("Signature is Invalid!")

# If the message is modified or the signature is incorrect,
# verification fails and InvalidSignature is raised.

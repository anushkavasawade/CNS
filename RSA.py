
# ==========================================
# ASSIGNMENT 1: RSA PERFORMANCE ANALYSIS
# ==========================================

# STEP 1: Import required libraries

import time
import os

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# time: Used to calculate execution time
# os: Used to generate random messages
# rsa: Used for RSA key generation
# padding: Used for secure RSA encryption
# hashes: Used for SHA-256 hashing


# STEP 2: Define different RSA key sizes and message sizes

key_sizes = [1024, 2048, 3072]

# RSA key sizes are measured in bits.
# Larger key sizes generally provide stronger security
# but require more processing time.

# Message sizes are measured in bits
message_sizes = [64, 128, 256, 384]


# STEP 3: Repeat experiment for each RSA key size

for key_size in key_sizes:

    # Start measuring key generation time
    start = time.perf_counter()

    # Generate 5 RSA key pairs to calculate average time
    for i in range(5):

        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size
        )

    # Calculate average key generation time
    key_time = (time.perf_counter() - start) / 5

    # Extract public key from private key
    # Public key is used for encryption
    # Private key is used for decryption
    public_key = private_key.public_key()

    print("\nRSA Key Size:", key_size)
    print("Key Generation Time:", key_time * 1000, "ms")


    # STEP 4: Test different message sizes

    for bits in message_sizes:

        # Generate random message
        # Divide by 8 because 1 byte = 8 bits
        # os.urandom() generates random bytes
        message = os.urandom(bits // 8)


        # STEP 5: Configure OAEP padding with SHA-256

        oaep = padding.OAEP(
            mgf=padding.MGF1(hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )

        # OAEP stands for Optimal Asymmetric Encryption Padding.
        # It adds secure padding to the message before encryption.
        # SHA-256 is used as the hashing algorithm.


        # STEP 6: Measure encryption time

        start = time.perf_counter()

        # Encrypt message 100 times using public key
        for i in range(100):

            ciphertext = public_key.encrypt(message, oaep)

        # Calculate average encryption time
        encrypt_time = (time.perf_counter() - start) / 100

        # Multiplying by 1000 converts seconds into milliseconds.


        # STEP 7: Measure decryption time

        start = time.perf_counter()

        # Decrypt ciphertext 100 times using private key
        for i in range(100):

            decrypted = private_key.decrypt(ciphertext, oaep)

        # Calculate average decryption time
        decrypt_time = (time.perf_counter() - start) / 100


        # STEP 8: Display results

        print("\nMessage Size:", bits, "bits")

        print("Encryption Time:",
              encrypt_time * 1000, "ms")

        print("Decryption Time:",
              decrypt_time * 1000, "ms")


        # STEP 9: Verify decrypted message

        # Check whether the decrypted message
        # is exactly the same as the original message.
        assert decrypted == message

        print("Message Verification Successful!")


# STEP 10: End of experiment

print("\nExperiment Completed!")


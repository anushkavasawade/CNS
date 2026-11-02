
# ==========================================
# ASSIGNMENT 9: SECURE IMAGE TRANSMISSION
# ==========================================

# STEP 1: Import the required library

from cryptography.fernet import Fernet

# Fernet is used for symmetric encryption and decryption.
# It provides confidentiality, integrity and authentication.


# STEP 2: Generate a secret key

key = Fernet.generate_key()

# Generate a random secret key.
# The same key is used for encryption and decryption.


# STEP 3: Create a cipher object using the secret key

cipher = Fernet(key)

# Create a Fernet object using the generated key.
# This object performs encryption and decryption.


# STEP 4: Read the original image

with open("image.png", "rb") as file:
    image_data = file.read()

# "rb" means read binary mode.
# Images are stored as binary data (bytes).
# read() loads the complete image data.


# STEP 5: Encrypt the image data

encrypted_image = cipher.encrypt(image_data)

# Fernet encrypts the original image data.
# AES-128 is used for encryption.
# HMAC-SHA256 checks data integrity and authenticity.
# The encrypted data cannot be viewed as the original image.


# STEP 6: Save the encrypted image

with open("encrypted_image.txt", "wb") as file:
    file.write(encrypted_image)

# "wb" means write binary mode.
# Save the encrypted data into a file.
# The original image is now stored in encrypted form.

print("Image Encrypted Successfully!")


# STEP 7: Decrypt the encrypted image

decrypted_image = cipher.decrypt(encrypted_image)

# Use the SAME secret key to decrypt the image.
# Fernet verifies the encrypted data before decryption.
# The original image data is recovered.


# STEP 8: Save the decrypted image

with open("decrypted_image.jpg", "wb") as file:
    file.write(decrypted_image)

# Save the recovered image in binary format.
# The decrypted image can now be opened and viewed.

print("Image Decrypted Successfully!")


# STEP 9: Display completion message

print("Secure Image Transmission Completed!")

# Image encryption and decryption process is completed.

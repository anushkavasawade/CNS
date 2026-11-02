
# ==========================================
# DIFFIE-HELLMAN KEY EXCHANGE WITH MITM ATTACK
# ==========================================

# STEP 1: Define public parameters

p = 23
g = 5

# p = Prime number
# g = Generator (primitive root)
# These values are public and can be shared with everyone.


# STEP 2: Define private keys

alice_private = 6
bob_private = 15

# Alice and Bob choose their own secret private keys.
# These keys must not be shared with anyone.


# STEP 3: Define Eve's private keys

eve_private_alice = 7
eve_private_bob = 11

# Eve is the attacker.
# She creates two different private keys:
# One to communicate with Alice and another with Bob.


print("DIFFIE-HELLMAN KEY EXCHANGE")
print("--------------------------------")


# STEP 4: Generate public keys

alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)

# Formula: Public Key = (g ^ private_key) mod p
#
# pow(base, exponent, modulus) performs
# modular exponentiation efficiently.
#
# Alice generates her public key.
# Bob generates his public key.

print("\nAlice Public Key:", alice_public)
print("Bob Public Key:", bob_public)


# STEP 5: Calculate normal shared secret

alice_shared = pow(bob_public, alice_private, p)
bob_shared = pow(alice_public, bob_private, p)

# Alice uses Bob's public key and her private key.
# Bob uses Alice's public key and his private key.
#
# Both should calculate the SAME shared secret.

print("\nNORMAL KEY EXCHANGE")
print("Alice Shared Secret:", alice_shared)
print("Bob Shared Secret:", bob_shared)

if alice_shared == bob_shared:
    print("Shared key established successfully!")


# -----------------------------------
# STEP 6: MAN IN THE MIDDLE ATTACK
# -----------------------------------

print("\n\nMAN-IN-THE-MIDDLE ATTACK")
print("--------------------------------")


# STEP 7: Eve generates two public keys

eve_public_alice = pow(g, eve_private_alice, p)
eve_public_bob = pow(g, eve_private_bob, p)

# Eve generates two public keys using her two private keys.
#
# She sends one public key to Alice
# and another public key to Bob.
#
# Alice and Bob unknowingly receive Eve's public keys
# instead of each other's actual public keys.

print("Eve Public Key for Alice:", eve_public_bob)
print("Eve Public Key for Bob:", eve_public_alice)


# STEP 8: Alice unknowingly shares a key with Eve

alice_eve_key = pow(
    eve_public_bob, alice_private, p
)

# Alice uses the public key received from Eve
# and her own private key to calculate a shared secret.


# STEP 9: Bob unknowingly shares a key with Eve

bob_eve_key = pow(
    eve_public_alice, bob_private, p
)

# Bob uses the public key received from Eve
# and his own private key to calculate a shared secret.


# STEP 10: Eve calculates the same two shared keys

eve_alice_key = pow(
    alice_public, eve_private_bob, p
)

eve_bob_key = pow(
    bob_public, eve_private_alice, p
)

# Eve uses Alice's actual public key with her private key
# to calculate the Alice-Eve shared secret.
#
# Eve uses Bob's actual public key with her other private key
# to calculate the Bob-Eve shared secret.


# STEP 11: Display all shared keys

print("\nAlice Shared Key:", alice_eve_key)
print("Eve-Alice Shared Key:", eve_alice_key)

print("\nBob Shared Key:", bob_eve_key)
print("Eve-Bob Shared Key:", eve_bob_key)


# STEP 12: Verify whether MITM attack is successful

if (alice_eve_key == eve_alice_key and
        bob_eve_key == eve_bob_key):

    print("\nMITM ATTACK SUCCESSFUL!")
    print("Eve has established separate keys with Alice and Bob.")
    print("Eve can intercept their communication.")

# If both pairs of shared keys match,
# Eve has successfully established separate
# shared secrets with Alice and Bob.

from pqcrypto.kem.ml_kem_512 import keygen, encaps, decaps

print("=== ML-KEM-512 Demo ===")

# Step 1: Generate a key pair
public_key, secret_key = keygen()

print("1. Key pair generated")
print("Public key size:", len(public_key), "bytes")
print("Secret key size:", len(secret_key), "bytes")

# Step 2: Encapsulate a shared secret
ciphertext, shared_secret = encaps(public_key)

print("2. Shared secret generated")
print("Ciphertext size:", len(ciphertext), "bytes")
print("Shared secret size:", len(shared_secret), "bytes")

# Step 3: Decapsulate the ciphertext
recovered_secret = decaps(secret_key, ciphertext)

print("3. Shared secret recovered")
print("Recovered secret size:", len(recovered_secret), "bytes")

# Step 4: Compare the two secrets
if shared_secret == recovered_secret:
    print("4. SUCCESS: Shared secrets match!")
else:
    print("4. ERROR: Shared secrets do not match!")

from pqcrypto.sign.ml_dsa_65 import keygen, sign, verify

print("=== ML-DSA-65 Post-Quantum Signature Demo ===")

# Step1 生成签名密钥对
public_key, secret_key = keygen()
print("1. Key pair generated")
print("Public key size:", len(public_key), "bytes")
print("Secret key size:", len(secret_key), "bytes")

# Step2 需要签名的消息（纯ASCII）
message = b"Post-quantum cryptography lab activity 3"

# Step3 使用私钥生成签名
signature = sign(secret_key, message)
print("2. Signature created")
print("Signature size:", len(signature), "bytes")

# Step4 使用公钥验证签名
try:
    verify(public_key, message, signature)
    print("3. SUCCESS: Signature verification passed!")
except:
    print("3. ERROR: Signature verification failed!")


# ML-KEM Python Project

## Description

This project demonstrates the ML‑KEM‑512 post‑quantum key encapsulation mechanism using Python and the pqcrypto library.

## How it works

1. Generate a public key and secret key.
2. Encapsulate a shared secret using the public key.
3. Decapsulate the ciphertext using the secret key.
4. Compare the original and recovered shared secrets.

If the two shared secrets match, the ML‑KEM process is successful.

## Installation

```bash
pip install pqcrypto

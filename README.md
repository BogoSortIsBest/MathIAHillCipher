# Math IA – Modern Encryption (Hill Cipher + RSA) + Hill Cipher Attack Demo

This repository contains the code and write-up for my Math IA: **“A Deep Dive Into Modern Encryption” (April 2022)**.

The IA explores:
- Substitution ciphers (ROT13 / Caesar)
- The **Hill cipher** (matrix multiplication mod 26), including **decryption via modular inverses**
- A practical vulnerability of the Hill cipher: **known-plaintext attacks**
- Intro to **RSA** and a proof sketch using Euler’s theorem

The Python code in `main.py` focuses on the Hill cipher portion and experimentally compares:
- **Brute-force key search** vs.
- **System-of-linear-equations attack** (using a few known plaintext characters)

## Files
- `main.py` — Hill cipher encrypt/decrypt + brute-force attack + known-plaintext linear-equation attack + timing “stress test”
- `Math_IA.pdf` — full IA write-up (linked below)

## Math IA PDF
- 📄 **Read the IA:** [Math_IA.pdf](Math_IA.pdf)

> GitHub doesn’t reliably render PDFs inline inside README, but the link above opens the PDF in GitHub’s viewer.

---

## What the program does (Hill Cipher demo)

### Hill cipher (2×2 key, mod 26)
- Text is treated as lowercase letters `a`–`z`
- Letters map to numbers `a=0, b=1, ..., z=25`
- Encryption multiplies each 2-letter block by a 2×2 key matrix (mod 26)

### Attacks compared
1. **Brute force**
   - Tries all possible 2×2 keys (in this implementation: all entries 0–25)
   - Checks which key decrypts the ciphertext back to the original message

2. **Known-plaintext linear-equation attack**
   - Assumes the attacker knows the first **four plaintext letters**
   - Builds 4 modular linear equations and solves for the key

The IA reports this attack is dramatically faster on average. (See the “Deciphering Approach Comparison” table in the PDF.)

---

## Requirements
- Python 3.x
- No external dependencies (uses only the standard library)

---

## How to run

```bash
python3 main.py

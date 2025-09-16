# GeneCrypt - Genetic obfuscation tool

# 🧬 GeneCrypt – Genetic obfuscation tool

**GeneCrypt** is a Python-based CLI tool that encodes and decodes text or files into DNA-style sequences (`A`, `T`, `G`, `C`) using a custom, reversible transformation pipeline.

It’s a blend of data compression, hashing, and genetic code-inspired encoding — designed to be both **secure and fun**.

---

## 🔐 Security Status

GeneCrypt is currently in **early beta**.

- ✅ The encoded data is **reversible only with the correct numeric key**
- 🔓 The encoding method is **decodable with effort** in its current form
- 🛡️ Future updates will improve security with:
  - Salted and non-deterministic key generation
  - Hybrid encryption support
  - Optional HMAC integrity checks

> ⚠️ Until then, consider GeneCrypt **secure for experimentation**, **prototyping**, and **creative applications** — but not for storing high-risk sensitive data.

---

## 📦 Features

- Convert any text or file to a DNA-style sequence (ATGC)
- Compress and encode input using zlib + base64
- Generate a numeric key using SHA-256 from a derived password
- Reversible decoding with the correct key
- File support for encryption/decryption
- Easy-to-use command line interface

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/genecrypt.git
cd genecrypt
````

Run with Python:

```bash
python genecrypt.py --help
```

---

## 🚀 Usage

### 🔐 Encrypt Text

```bash
python genecrypt.py -m encrypt -t text -i "Hello, World!"
```

### 🔐 Encrypt File

```bash
python genecrypt.py -m encrypt -t file -i example.txt
```

### 🔓 Decrypt Text

```bash
python genecrypt.py -m decrypt -t text -i <GENETIC_CODE> -p <NUMERIC_SECRET>
```

### 🔓 Decrypt File

```bash
python genecrypt.py -m decrypt -t file -i example.txt -p <NUMERIC_SECRET>
```

---

## 🧪 How It Works

1. Compress input with zlib and encode with base64
2. Convert to binary and then into DNA-style bases (A=00, T=01, G=10, C=11)
3. Generate the complement of the sequence
4. Decode complement back to a password
5. Hash and convert password into a numeric key
6. Use key to encode original text into the final genetic string

---

## 🔗 Roadmap

* [ ] Non-deterministic output with salt
* [ ] Optional AES-256 hybrid encryption layer
* [ ] Built-in HMAC for integrity verification
* [ ] Web-based UI (coming soon!)

---

## 💡 Example

```
Input: "Hello, World!"
➡ Genetic Code: ATGCTAGTC...
➡ Complement: TACGATCAG...
➡ Final DNA Code: TGCAAGT...
➡ Use secret to decode
```

---

## 🧑‍💻 Author

Created by [Adhwaith A S](https://github.com/adhwaithas)

## Support

If you like this project, consider [Buying me a coffee](https://buymeacoffee.com/adhwaithas) ☕.

---

## 📜 License

This project is licensed under the [Apache License 2.0](LICENSE).

© 2025 Adhwaith A S. You must retain attribution to the original author when using or modifying this code.

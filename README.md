# GeneCrypt - Genetic obfuscation tool
````markdown
# 🧬 GeneCrypt - Genetic obfuscation tool

**GeneCrypt** is a fun and educational CLI tool that encodes and decodes text or files into a DNA-like format (`A`, `T`, `G`, `C`) using reversible transformations. It provides a creative way to obfuscate data by simulating genetic encoding principles.

> ⚠️ **Note**: This tool is for **obfuscation and educational purposes** only. It is **not cryptographically secure** and should not be used to store or transmit sensitive data.

---

## 📦 Features

- Encode plain text into DNA-style sequences
- Derive a numeric key from the encoded DNA
- Reconstruct original text using the numeric key
- File encryption and decryption support
- CLI interface for flexible usage

---

## 🛠️ Installation

Clone the repository and navigate into the directory:

```bash
git clone https://github.com/your-username/genecrypt.git
cd genecrypt
````

Run the script using Python 3:

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
python genecrypt.py -m encrypt -t file -i message.txt
```

### 🔓 Decrypt Text

```bash
python genecrypt.py -m decrypt -t text -i <GENETIC_CODE> -p <NUMERIC_SECRET>
```

### 🔓 Decrypt File

```bash
python genecrypt.py -m decrypt -t file -i message.txt -p <NUMERIC_SECRET>
```

---

## 🧬 How It Works

1. Text is compressed and encoded using Base64 and zlib.
2. It is then converted into a binary string and mapped to the genetic bases:

   * `00` → A
   * `01` → T
   * `10` → G
   * `11` → C
3. The complement of this genetic string is generated.
4. This complement is reversed to derive a pseudo-password.
5. The password is compressed and hashed with SHA-256, and a numeric secret is derived.
6. This numeric secret is used to alter the original encoded integer and generate the final DNA string.

---

## 📄 Example

```bash
[+] Genetic Code: ATGCTAGTCGAT...
[+] Complement Code: TACGATCAGCTA...
[+] Extracted Password: ...
[+] Numeric Encoded Secret: 23948512
[+] Final Genetic Code with Key: TGACGTAGCTAG...
```

To decrypt, supply the final genetic code and the numeric secret:

```bash
python genecrypt.py -m decrypt -t text -i TGACGTAGCTAG... -p 23948512
```

---

## ⚠️ Disclaimer

This tool does **not** use industry-standard encryption algorithms. Do **not** use it for securing real passwords, sensitive information, or any critical data.

---

## 🧑‍💻 Author

Created by [Adhwaith A S](https://github.com/adhwaithas)

## Support

If you like this project, consider [Buying me a coffee](https://buymeacoffee.com/adhwaithas) ☕.

---

## 📜 License

This project is licensed under the [Apache License 2.0](LICENSE).

© 2025 Adhwaith A S. You must retain attribution to the original author when using or modifying this code.

```

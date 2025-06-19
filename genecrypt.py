import argparse
import base64
import binascii
import zlib
import os
import hashlib


def compress_and_encode(text):
    compressed = zlib.compress(text.encode())
    return base64.urlsafe_b64encode(compressed).decode()


def decode_and_decompress(encoded):
    compressed = base64.urlsafe_b64decode(encoded.encode())
    return zlib.decompress(compressed).decode()


def text_to_genetic(text):
    hex_str = binascii.hexlify(text.encode())
    bin_str = bin(int(hex_str, 16))[2:].zfill(8 * ((len(hex_str) + 1) // 2))
    return ''.join(['ATGC'[int(bin_str[i:i + 2], 2)] for i in range(0, len(bin_str), 2)])


def text_to_genetic_with_password(text, password):
    hex_str = binascii.hexlify(text.encode())
    hex_int = int(hex_str, 16)
    updated_int = hex_int + int(password)
    updated_hex = f"{updated_int:x}".zfill(len(hex_str))
    bin_str = bin(int(updated_hex, 16))[2:].zfill(
        8 * ((len(updated_hex) + 1) // 2))
    return ''.join(['ATGC'[int(bin_str[i:i + 2], 2)] for i in range(0, len(bin_str), 2)])


def complement_sequence(seq):
    comp_map = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(comp_map[i] for i in seq)


def genetic_to_text(genetic_code):
    bin_str = ''.join({
        'A': '00', 'T': '01', 'G': '10', 'C': '11'
    }[c] for c in genetic_code)
    chars = [chr(int(bin_str[i:i + 8], 2)) for i in range(0, len(bin_str), 8)]
    return ''.join(chars)


def key_encoding(password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    short_hex = hashed[:8]
    return str(int(short_hex, 16))


def encrypt_text_mode(text):
    vault = text_to_genetic(text)
    print("[+] Genetic Code:", vault)

    complement = complement_sequence(vault)
    print("[+] Complement Code:", complement)

    password = genetic_to_text(complement)
    print("[+] Extracted Password:", password)

    secret = key_encoding(compress_and_encode(password))
    print("[+] Numeric Encoded Secret:", secret)

    final_genetic = text_to_genetic_with_password(text, secret)
    print("[+] Final Genetic Code with Key:", final_genetic)


def encrypt_file_mode(filepath):
    if not os.path.isfile(filepath):
        print("[-] File does not exist.")
        return

    with open(filepath, 'r') as f:
        content = f.read()
    print("[*] File Content:\n", content)

    vault = text_to_genetic(content)
    complement = complement_sequence(vault)
    password = genetic_to_text(complement)
    secret = key_encoding(compress_and_encode(password))
    print("[+] Numeric Encoded Secret:", secret)

    final_genetic = text_to_genetic_with_password(content, secret)

    with open(filepath, 'w') as f:
        f.write(final_genetic)

    print("[+] Encrypted Genetic Code written to file.")


def decrypt_genetic_code_with_numeric_secret(genetic_code, numeric_secret):
    print("[*] Decrypting Final Genetic Code with Numeric Secret...")

    bin_str = ''.join({'A': '00', 'T': '01', 'G': '10', 'C': '11'}[
                      c] for c in genetic_code)
    encoded_int = int(bin_str, 2)

    original_int = encoded_int - int(numeric_secret)
    original_hex = f"{original_int:x}"
    if len(original_hex) % 2 != 0:
        original_hex = '0' + original_hex

    try:
        original_bytes = binascii.unhexlify(original_hex)
        original_text = original_bytes.decode()
        print("[+] Decrypted Original Text:", original_text)
    except Exception as e:
        print("[-] Decryption failed:", str(e))


def decrypt_file_mode(filepath, numeric_secret):
    if not os.path.isfile(filepath):
        print("[-] File does not exist.")
        return

    with open(filepath, 'r') as f:
        genetic_code = f.read().strip()

    print("[*] Genetic Code from File:\n", genetic_code)

    # Convert genetic code to binary
    bin_str = ''.join({'A': '00', 'T': '01', 'G': '10', 'C': '11'}[
                      c] for c in genetic_code)
    encoded_int = int(bin_str, 2)

    try:
        original_int = encoded_int - int(numeric_secret)
        original_hex = f"{original_int:x}"
        if len(original_hex) % 2 != 0:
            original_hex = '0' + original_hex

        original_bytes = binascii.unhexlify(original_hex)
        original_text = original_bytes.decode()
        print("[+] Decrypted Original Text:\n", original_text)

        with open(filepath, 'w') as f:
            f.write(original_text)
        print("[+] File content replaced with decrypted text.")

    except Exception as e:
        print("[-] Decryption failed:", str(e))


def main():
    parser = argparse.ArgumentParser(description="GeneCrypt CLI Tool")
    parser.add_argument(
        "-m", "--mode", choices=["encrypt", "decrypt"], required=True, help="Mode: encrypt or decrypt")
    parser.add_argument(
        "-t", "--type", choices=["text", "file"], required=True, help="Type of input: text or file")
    parser.add_argument("-i", "--input", required=True,
                        help="Input text, genetic code, or file path")
    parser.add_argument("-p", "--password", required=False,
                        help="Password (for decrypting final code)")

    args = parser.parse_args()

    if args.mode == "encrypt":
        if args.type == "text":
            encrypt_text_mode(args.input)
        elif args.type == "file":
            encrypt_file_mode(args.input)

    elif args.mode == "decrypt":
        if not args.password:
            print("[-] Please provide the numeric secret using -p.")
            return
        if args.type == "text":
            decrypt_genetic_code_with_numeric_secret(args.input, args.password)
        elif args.type == "file":
            decrypt_file_mode(args.input, args.password)


if __name__ == "__main__":
    main()

def encrypt_char(char, shift1, shift2):
    if char.islower():
        if 'a' <= char <= 'm':
            shift = shift1 * shift2
            return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif 'n' <= char <= 'z':
            shift = -(shift1 + shift2)
            return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    elif char.isupper():
        if 'A' <= char <= 'M':
            shift = -shift1
            return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif 'N' <= char <= 'Z':
            shift = shift2 ** 2
            return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    else:
        return char

def decrypt_char(char, shift1, shift2):
    if char.islower():
        if 'a' <= char <= 'm':
            shift = -(shift1 * shift2)
            return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif 'n' <= char <= 'z':
            shift = shift1 + shift2
            return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    elif char.isupper():
        if 'A' <= char <= 'M':
            shift = shift1
            return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif 'N' <= char <= 'Z':
            shift = -(shift2 ** 2)
            return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    else:
        return char

def encrypt_file(shift1, shift2):
    with open("raw_text.txt", "r") as infile, open("encrypted_text.txt", "w") as outfile:
        for line in infile:
            encrypted_line = ''.join(encrypt_char(char, shift1, shift2) for char in line)
            outfile.write(encrypted_line)

def decrypt_file(shift1, shift2):
    with open("encrypted_text.txt", "r") as infile, open("decrypted_text.txt", "w") as outfile:
        for line in infile:
            decrypted_line = ''.join(decrypt_char(char, shift1, shift2) for char in line)
            outfile.write(decrypted_line)

def verify_decryption():
    with open("raw_text.txt", "r") as original, open("decrypted_text.txt", "r") as decrypted:
        original_content = original.read()
        decrypted_content = decrypted.read()
        if original_content == decrypted_content:
            print("✅ Decryption was successful! The files match.")
        else:
            print("❌ Decryption failed. The files do not match.")

def main():
    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))

    print("Encrypting the file...")
    encrypt_file(shift1, shift2)

    print("Decrypting the file...")
    decrypt_file(shift1, shift2)

    print("Verifying decryption...")
    verify_decryption()

if __name__ == "__main__":
    main()

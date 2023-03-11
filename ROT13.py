plaintext = input("Enter text to encrypt/decrypt : ")

def rot13(text):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 13 if char.islower() else -13
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            new_char = char
        result += new_char
    return result

ciphertext = rot13(plaintext)
print(ciphertext)

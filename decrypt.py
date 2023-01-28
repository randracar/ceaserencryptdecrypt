def decrypt_caesar(ciphertext, shift):
    # Initialize an empty string to store the plaintext
    plaintext = ""
    # Iterate over each character in the ciphertext
    for char in ciphertext:
        # Check if the character is a letter
        if char.isalpha():
            # Check if the character is uppercase or lowercase
            if char.isupper():
                # For uppercase letters, shift the character by the given shift value and convert it back to a letter
                # The modulo operator is used to wrap around if the shift goes beyond the range of letters
                shift_value = (ord(char) - shift - 65) % 26 + 65
            else:
                # For lowercase letters, shift the character by the given shift value and convert it back to a letter
                # The modulo operator is used to wrap around if the shift goes beyond the range of letters
                shift_value = (ord(char) - shift - 97) % 26 + 97
            # Add the decrypted letter to the plaintext string
            plaintext += chr(shift_value)
        else:
            # For non-letter characters, add the character to the plaintext string as is
            plaintext += char
    # Return the plaintext
    return plaintext

# Get the ciphertext from the user
ciphertext = input("Input:")
# Get the shift value from the user
shift = int(input("Shift:"))
# Decrypt the ciphertext
plaintext = decrypt_caesar(ciphertext, shift)
# Print the plaintext
print(plaintext)
def encrypt_caesar(plaintext, shift):
    # Initialize an empty string to store the ciphertext
    ciphertext = ""
    # Iterate over each character in the plaintext
    for char in plaintext:
        # Check if the current character is a letter
        if char.isalpha():
            # Shift the character's ASCII value by the specified shift value
            shift_value = ord(char) + shift
            # Check if the current character is uppercase
            if char.isupper():
                # Check if the shifted ASCII value is greater than the ASCII value of 'Z'
                if shift_value > ord('Z'):
                    # If so, subtract 26 from the shifted ASCII value to wrap around to the beginning of the alphabet
                    shift_value -= 26
                # Add the shifted character to the ciphertext
                ciphertext += chr(shift_value)
            else:
                # Check if the shifted ASCII value is greater than the ASCII value of 'z'
                if shift_value > ord('z'):
                    # If so, subtract 26 from the shifted ASCII value to wrap around to the beginning of the alphabet
                    shift_value -= 26
                # Add the shifted character to the ciphertext
                ciphertext += chr(shift_value)
        else:
            # If the current character is not a letter, add it to the ciphertext unmodified
            ciphertext += char
    # Return the final ciphertext
    return ciphertext

# Get the plaintext and shift value from the user
plaintext = input("Input:")
shift = int(input("Shift:"))
# Encrypt the plaintext with the Caesar Cipher
ciphertext = encrypt_caesar(plaintext, shift)
# Print the resulting ciphertext
print(ciphertext)
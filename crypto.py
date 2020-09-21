# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
	encription = ""
	for element in plaintext
		newUnicde = ((ord(element) - 65 + offset) % 26) + 65
		encription.append(chr(newUnicode))
	return encription

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    pass
	originalPlainText = ""
	for element in ciphertext
		if (ord(element) - 65 - offset < 0)
			newUnicde = (ord(element) - 65 + 26 - offset) + 65
			encription.append(chr(newUnicode))
		elif
			newUnicde = (ord(element) - 65 - offset) + 65
			encription.append(chr(newUnicode))
	return originalPlainText 

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    pass

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    pass

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    pass

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    pass

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():
    # Testing code here
    pass

if __name__ == ‘__main__’:
    main()

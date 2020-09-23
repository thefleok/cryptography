# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
	encription = ""
	for element in plaintext:
		newUnicode = ((ord(element) - 65 + offset) % 26) + 65
		encription = encription + chr(newUnicode)
	return encription

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
	originalPlainText = ""
	for element in ciphertext:
		if ord(element) - 65 - offset < 0:
			newUnicode = (ord(element) - 65 + 26 - offset) + 65
			encription.append(chr(newUnicode))
		else:
			newUnicde = (ord(element) - 65 - offset) + 65
			encription.append(chr(newUnicode))
	return originalPlainText 
# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
	encription = ""
	truIndex = 0
	for element in plaintext:
		ogUnicode = ord(element) - 65
		keyUnicode = ord(keyword[index]) - 65
		encription.append(chr((ogUnicode + keyUnicode) % 26 + 65))
		truIndex = truIndex + 1
	return encription
# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
	encription = ""
	truIndex = 0
	for element in ciphertext:
		ogUnicode = ord(element) - 65
		keyUnicode = ord(keyword[truIndex]) - 65
		if ord(element) - 65 - keyUnicode < 0:
			newUnicode = (ord(element) - 65 + 26 - keyUnicode) + 65
			encription.append(chr(newUnicode))
			index = index + 1
		else:
			newUnicode = (ord(element) - 65 - keyUnicode) + 65
			encription.append(chr(newUnicode))
			index = index + 1
	return encription

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
	Legend = encrypt_caesar("AAA", 4)
	print (Legend)
	print (decrypt_caesar(Legend, 4)
	BloodyLegend = encrypt_vigenere

main()

import random
import math

# Caesar Cipher
# Arguments: string, integer
# Returns: string

def encrypt_caesar(plaintext, offset):
    encription = ""
    # this loop iterates across plaintext and displaces letters by offset
    for element in plaintext:
        if not element.isalpha():
            new_unicode = ord(element)
        else:
            new_unicode = ((ord(element) - 65 + offset) % 26) + 65
        encription = encription + chr(new_unicode)
    return encription

# Arguments: string, integer
# Returns: string

def decrypt_caesar(ciphertext, offset):
    original_plaintext = ""
    # this loop traverses cyphertext and displaces based on offset letter value
    for element in ciphertext:
        if not element.isalpha():
            original_plaintext = original_plaintext + element
        else:
            if ord(element) - 65 - offset < 0: # goes to back of alphabet
                new_unicode = ord(element) + 26 - offset
                original_plaintext = original_plaintext + (chr(new_unicode))
            else: # goes backwards through alphabet, but never a to z
                new_unicode = ord(element) - offset
                original_plaintext = original_plaintext + (chr(new_unicode))
    return original_plaintext 

# Vigenere Cipher
# Arguments: string, string
# Returns: string

def encrypt_vigenere(plaintext, keyword):
    while len(keyword) < len(plaintext): # keyword length >= plaintext length 
        keyword = keyword + keyword
    encription = ""
    index = 0 # index for the keyword being encrypted
    # for loop encrypts plaintext by offset determined by letter value
    for element in plaintext:
        original_unicode = ord(element) - 65
        key_unicode = ord(keyword[index]) - 65
        encription = encription + (chr((original_unicode + key_unicode) % 26 
                     + 65))
        index = index + 1
    return encription

# Arguments: string, string
# Returns: string

def decrypt_vigenere(ciphertext, keyword):
    while len(keyword) < len(ciphertext): # same function as in encrypt method
        keyword = keyword + keyword
    encription = ""
    index = 0
    # for loop decodes ciphertext using keyword, if same keyword as encryption
    for element in ciphertext:
        original_unicode = ord(element) - 65
        key_unicode = ord(keyword[index]) - 65
        # if statemenets determine if decrypt goes past 0
        if ord(element) - 65 - key_unicode < 0:
            new_unicode = (ord(element) - 65 + 26 - key_unicode) + 65
            encription = encription +(chr(new_unicode))
            index = index + 1
        else:
            new_unicode = (ord(element) - 65 - key_unicode) + 65
            encription = encription + (chr(new_unicode))
            index = index + 1
    return encription

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both  integers

def generate_private_key(n=8):
    W = (1,) # tuple of W starts with 1
    count = 0
    # while loop that randomly generates superincreasing list
    while count < n - 1:
        totality = sum(list(W))
        addition = random.randint(totality + 1, totality*2)
        W = W + (addition,)
        count = count + 1
    Q = random.randint(sum(list(W)) + 1, 2 * sum(list(W)))
    R = 0
    while (math.gcd(Q,R) != 1): # generates random value R until coprime
        R = random.randint(2, Q - 1)
    private_key = (W, Q, R)
    return private_key 

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers

def create_public_key(private_key):
    W = private_key [0]
    Q = private_key [1]
    R = private_key [2]
    B = ()
    # creates B, which is function of W, Q, and R, as public key
    for x in W:
        B = B + ((R*x) % Q,)
    return B

# Arguments: int
# Returns: tuple of bits

def byte_to_bits(value):
    bits = [0, 0, 0, 0, 0, 0, 0, 0]
    count = 7
    # loop changes values to 1 if they can fit from highest to lowest
    while count >= 0:
        if (value - (2**count)) >= 0: # if that bit can fit in the byte
            value = value - 2**count
            bits[count] = 1
        count = count - 1
    bits_tuple = tuple(bits)
    return bits_tuple

# Arguments: tuple
# Returns: Byte from tuple of bits

def bits_to_byte(bits):
    byte = 0
    count = 0
    # while loop grabs each bit and applies appropriate exponent
    while count < 8:
        if bits [count] == 1: # non zero value
            byte = byte + 2**count
        count = count + 1
    return byte

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers

def encrypt_mhkc(plaintext, public_key):
    encryption = ()
    # for loop runs through plaintext and converts each into 8 bit unicode
    for element in plaintext:
        bits_form = byte_to_bits(ord(element))
        C = 0
        count = 0
        for x in bits_form:
            C = C + x * public_key[count]
            count = count + 1 # increases index each time
        encryption = encryption + (C,) # add C for each letter
    return list(encryption)

# Arguments: int R, int Q
# Returns: value for S

def find_S (Q, R):
    S = 0
    # finds S through random guess and check till satisfying condition
    while R*S % Q != 1:
        S = S + 1
    return S

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext

def decrypt_mhkc(ciphertext, private_key):
    C = ()
    C = tuple(ciphertext)
    C_prime = ()
    # for loop finds S and builds c prime component
    for x in C:
        S = find_S(private_key[1], private_key[2])
        C_prime = C_prime + ((x*S % private_key[1]),)
    W = private_key[0]
    bytearray = ()
    # for loop converts to appropriate bits for unicode
    for x in C_prime:
        bits = [0, 0, 0, 0, 0, 0, 0, 0]
        count = 7
        while count >= 0:
            if (x - W[count]) >= 0:
                x = x - W[count]
                bits[count] = 1
            count = count - 1
        bits_tuple = tuple(bits)
        bytearray = bytearray + (bits_to_byte(bits_tuple),)
    return bytearray_to_string(bytearray)

# Arguments: bytearray of character values
# Returns: A string determined by those values

def bytearray_to_string(bytearray):
    # gets final string value
    finalString = ""
    for x in bytearray:
        finalString = finalString + chr(x)
    return finalString

# Main function, executes code

if __name__ == "__main__":
    # main method with test code
    str = "A,ONEINPUT,O"
    listo = str.split (",")
    li = []
    for element in listo:
        if element.isdigit():
            li.append(int(element))
        else:
            li.append(element)
    if li[1].isdigit():
        caesarEncryption = encrypt_caesar(li[0], li[1])
        caesarDecryption = decrypt_caesar(caesarEncryption, li[1])
        if (caesarDecryption == li[0]) & (caesarEncryption == li[2]):
            print("caesar true")
    oneone = encrypt_vigenere(li[0], li[1])
    zero = decrypt_vigenere(oneone, li[1])
    if (zero == li[0]) & (oneone == li[2]):
        print ("vigenere true")
    privatekey = generate_private_key()
    publickey = create_public_key(privatekey)
    encryption = encrypt_mhkc("Matthew Redmond", publickey)
    outcome = decrypt_mhkc(encryption, privatekey)
    print (outcome)
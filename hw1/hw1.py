import numpy as np
from sympy import Matrix
'''
Frank Lee
CS178: HW1 problems
'''


def caesar_cipher_decrypt(cipher="", key=None):
    # encoding of a-z is 97-122
    cipher_lower = cipher.lower()
    if not key:
        for keys in range(26):
            decrypted = ""
            for char in cipher_lower:
                if ord(char) >= 97 and ord(char) <= 122:
                    decrypted += chr(((ord(char) - 97 - keys) % 26) + 97)
                if ord(char) == 32:
                    decrypted += ' '
            print("key {}: {}".format(keys, decrypted))
    else:
        decrypted = ""
        for char in cipher_lower:
            if ord(char) >= 97 and ord(char) <= 122:
                decrypted += chr(((ord(char) - 97 - key) % 26) + 97)
            if ord(char) == 32:
                decrypted += ' '
        print("provided key {}: {}".format(key, decrypted))


def vigenere_cipher_encrypt(plain_txt="", key=None):
    if not key:
        print("error: must provide non-empty key")
        exit(1)
    plain_txt_lower = plain_txt.lower()
    key = key.lower()
    encrypted = ""
    key_ix = 0
    for char in plain_txt_lower:
        if ord(char) >= 97 and ord(char) <= 122:
            # do encryption
            encrypted += chr(((ord(char) - 97 +
                               ord(key[key_ix]) - 97) % 26) + 97)
            key_ix = (key_ix + 1) % len(key)
        else:
            encrypted += char
    print("Encrypted: {}".format(encrypted))


def hill_cipher_encrypt(plain_txt="", key=None, d=None):
    # first place key into a dxd matrix
    if d == None:
        print("Error: must provide d value")
        exit(1)
    plain_txt = "".join(c for c in plain_txt.lower() if c.isalnum())
    key = key.lower()
    if len(key) != (d*d):
        print("Error: key length and d value mismatch")
        exit(1)
    if len(plain_txt) % d != 0:
        print("Patching plain text due to length mismatch...")
        number_of_patches = -len(plain_txt) % d
        for _ in range(number_of_patches):
            plain_txt += 'z'
        print("...done patching")
    A = np.array([[0 for _ in range(d)] for _ in range(d)])
    running_ix = 0
    encrypted = ""
    for i in range(d):
        for j in range(d):
            A[i][j] = ord(key[running_ix]) - 97
            running_ix += 1
    ix = 0
    while ix < len(plain_txt):
        v = np.array([ord(c)-97 for c in plain_txt[ix:ix+d]])
        Av = np.matmul(A, v) % 26
        encrypted += "".join([chr(val + 97) for val in Av]) + " "
        ix += d
    print("Encrypted: {}".format(encrypted))


def hill_cipher_decrypt(cipher_txt="", key=None, d=None):
    # first place key into a dxd matrix
    if d == None:
        print("Error: must provide d value")
        exit(1)
    cipher_txt = "".join(c for c in cipher_txt.lower() if c.isalnum())
    key = key.lower()
    if len(key) != (d*d):
        print("Error: key length and d value mismatch")
        exit(1)
    A = np.array([[0 for _ in range(d)] for _ in range(d)])
    running_ix = 0
    decrypted = ""
    for i in range(d):
        for j in range(d):
            A[i][j] = ord(key[running_ix]) - 97
            running_ix += 1
    # invert
    A = Matrix(A)
    A = A.inv_mod(26)
    ix = 0
    while ix < len(cipher_txt):
        v = np.array([ord(c)-97 for c in cipher_txt[ix:ix+d]])
        Av = np.matmul(A, v) % 26
        decrypted += "".join([chr(val + 97) for val in Av]) + " "
        ix += d
    print("Decrypted: {}".format(decrypted))


def problem_6_4_2():
    temp = [[-13, 6, -5], [-4, -4, 9], [-2, 15, 2]]
    A = Matrix(temp)
    A = A.inv_mod(26)
    B = np.array([[-17, 6, -15], [-2, 9, 3], [-18, -17, -16]])
    print(np.matmul(B, np.array(A)) % 26)


if __name__ == "__main__":
    # cipher1 = "many cheerful facts about the square of the hypotenuse"
    # cipher2 = "whoma demet hegen iusia mtoda ythem athem atici"
    # vigenere_cipher_encrypt(cipher1, "MATH")
    # vigenere_cipher_encrypt(cipher2, "SPIDER")
    # cipher3 = "Why, sometimes I’ve believed as many as six impossible things before breakfast!"
    # hill_cipher_encrypt(cipher3, key="PORCUPINE", d=3)
    # test = "eyz uck uoz wkm ocp yna nvs yqt wqo lma iwu lwy zik jds yxi wfe vxa egx qzk zkg mqp zlx"
    test2 = "VCKUP EDOPS JICJP NBZCV DDMKI IRQKP WAKQI QMJEX HSQAH XHSZX LCTC"
    hill_cipher_decrypt(test2, key="JACKFRUIT", d=3)

    # hill_cipher_encrypt("rhinocerosjc", key="TANGERINE", d=3)

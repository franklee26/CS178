def encrypt(file_name=None, output_file_name="encrypted.txt", key=0xF5F):
    if not file_name:
        print("Error: no file provided")
        exit(1)
    # encrypt
    with open(file_name, "r") as file:
        byte_array = bytearray(file.read(), encoding='utf8')
        for i in range(len(byte_array)):
            byte_array[i] ^= (key % 256)
    # write to new file
    with open(output_file_name, "wb") as file:
        file.write(bytearray(byte_array))


def decrypt(file_name="encrypted.txt", output_file_name="decrypted.py", key=0xF5F):
    with open(file_name, "rb") as file:
        byte_array = bytearray(file.read())
        for i in range(len(byte_array)):
            byte_array[i] ^= (key % 256)
    # write to output
    with open(output_file_name, "w") as file:
        file.write(str(byte_array.decode()))


if __name__ == "__main__":
    print("Starting Frank's HW encryption/decryption script...")
    while (1):
        print()
        decision = input(
            "Would you like to encrypt (e), decypt (d) or quit (q)? ")
        if decision == "e":
            file_name = input(
                "Please input the relative file path you wish to encrypt: ")
            key = input(
                "Please input the key (in hex form 0x...): ")
            key_int = int(key, 16)
            encrypt(file_name, key=key_int)
            print("Successfully encrypted to encrypted.txt")
        elif decision == "d":
            file_name = input(
                "Please input the relative file path you wish to decrypt (must be a .txt file): ")
            key = input(
                "Please input the key (in hex form 0x...): ")
            key_int = int(key, 16)
            decrypt(file_name, key=key_int)
            print("Successfully decrypted to decrypted.py")
        elif decision == "q":
            print("Exiting...")
            exit(0)
        else:
            print("Invalid option selected\n")

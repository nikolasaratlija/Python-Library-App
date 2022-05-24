""" An encryption mechanism based on the Caesar Cypher technique """

key = 5  # 'secret' key for the caesar cypher


def encrypt(file_to_encrypt):
    # target file to encrypt
    file = open(f"src/database/{file_to_encrypt}", "rb")
    byte_array = file.read()
    file.close()

    # perform bitwise operation to shift bytes
    encrypted_byte_list = [value ^ key for index, value in enumerate(byte_array)]

    # write encrypted bytes to new file
    encrypted_file = open(f"src/database/ENCRYPTED-{file_to_encrypt}", "wb+")
    encrypted_file.write(bytearray(encrypted_byte_list))
    encrypted_file.close()


def decrypt(file_to_decrypt):
    pass

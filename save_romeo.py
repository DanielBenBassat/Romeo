"""
author: Daniel Ben-Bassat
program name: save romeo
description: the program gets parameter, if "encrypt" the program recivies input and encrypts it into a file
                if "decrypt" the program the decrypts the sentence in the file and print it
date= 29.9.2023
"""

import sys

import logging
import os

# constants
LOG_FORMAT = '%(levelname)s | %(asctime)s | %(message)s'
LOG_LEVEL = logging.DEBUG
LOG_DIR = 'log'
LOG_FILE = LOG_DIR + '/lucky.log'


MSG1 = "My bounty is as boundless as the sea, My love as deep; the more I give to thee, The more I have, for both are infinite."

MSG2 = "Don't waste your love on somebody, who doesn't value it."

ENC1 = "48,96,98,13,36,92,35,91,96,98,30,90,98,12,90,98,13,36,92,35,15,33,16,90,90,98,12,90,98,91,19,16,98,90,16,12,99," \
      "98,48,96,98,33,36,93,16,98,12,90,98,15,16,16,37,101,98,91,19,16,98,34,36,39,16,98,44,98,18,30,93,16,98,91,36,98,91,19," \
      "16,16,99,98,65,19,16,98,34,36,39,16,98,44,98,19,12,93,16,99,98,17,36,39,98,13,36,91,19,98,12,39,16,98,30,35,17,30,35,30,91,16,100"

ENC2 = "59,36,35,102,91,98,94,12,90,91,16,98,96,36,92,39,98,33,36,93,16,98,36,35,98,90,36,34,16,13,36,15,96,99,98,94,19,36,98,15,36,16,90,35,102," \
      "91,98,93,12,33,92,16,98,30,91,100"

# functions


encrypt_dict = {"A": 56, "B": 57, "C": 58, "D": 59, "E": 40, "F": 41, "G": 42, "H": 43, "I": 44, "J": 45, "K": 46,
                "L": 47, "M": 48,
                "N": 49, "O": 60, "P": 61, "Q": 62, "R": 63, "S": 64, "T": 65, "U": 66, "V": 67, "W": 68, "X": 69,
                "Y": 10, "Z": 11,
                "a": 12, "b": 13, "c": 14, "d": 15, "e": 16, "f": 17, "g": 18, "h": 19, "i": 30, "j": 31, "k": 32,
                "l": 33, "m": 34,
                "n": 35, "o": 36, "p": 37, "q": 38, "r": 39, "s": 90, "t": 91, "u": 92, "v": 93, "w": 94, "x": 95,
                "y": 96, "z": 97,
                " ": 98, ",": 99, ".": 100, ";": 101, "'": 102, "?": 103, "!": 104, ":": 105}

decrypt_dict = {}
for key, value in encrypt_dict.items():
    decrypt_dict[value] = key


def encrypt():
    """
    get a message and turn it into number according to incription and write it in file
    """

    message = input("enter text: ")
    logging.debug('the message: ' + message)
    encrypted_msg = []

    for i in message:
        encrypted_msg.append(str(encrypt_dict[i]))
    encrypted_msg = ",".join(encrypted_msg)
    logging.debug('the encrypted message ' + encrypted_msg)

    file = open(r"C:\Users\User\OneDrive\מסמכים\דניאל\פייטון יא\romeo/encryped_msg.txt", "w")
    file.write(encrypted_msg)
    file.close()


def decrypt():
    """
    read the encrypted message from the file and turm the numbers into the massage
    :return: the decrypted massage
    """

    file = open(r"C:\Users\User\OneDrive\מסמכים\דניאל\פייטון יא\romeo/encryped_msg.txt", "r")
    encrypted_msg = file.read()
    logging.debug('the encrypted message ' + encrypted_msg)
    file.close()
    decrypted_msg = ""
    encrypted_msg = encrypted_msg.split(",")
    for i in encrypted_msg:
        if i != '':
            decrypted_msg += decrypt_dict[int(i)]
    logging.debug('the original message: ' + decrypted_msg)
    return decrypted_msg


def valid_parameter():
    return sys.argv[1] == "encrypt" or sys.argv[1] == "decrypt"


def check_encrypt(msg):
    encrypted_msg_check = []

    for i in msg:
        encrypted_msg_check.append(str(encrypt_dict[i]))

    return ",".join(encrypted_msg_check)


def main():

    if sys.argv[1] == "encrypt":
        encrypt()
    elif sys.argv[1] == "decrypt":
        print(decrypt())


if __name__ == '__main__':
    assert valid_parameter()
    assert check_encrypt(MSG1) == ENC1
    assert check_encrypt(MSG2) == ENC2

    if not os.path.isdir(LOG_DIR):
        os.makedirs(LOG_DIR)
    logging.basicConfig(format=LOG_FORMAT, filename=LOG_FILE, level=LOG_LEVEL)
    main()
"""
author: Daniel Ben-Bassat
program name: save romeo
description: the program gets parameter, if "encrypt" the program recivies input and encrypts it into a file
                if "decrypt" the program the decrypts the sentence in the file and print it
date= 29.9.2023
"""

import sys

#functions

def encrypt(): #הצפנה
    encrypt_dict = {"A": 56, "B": 57, "C": 58, "D": 59, "E": 40, "F": 41, "G": 42, "H": 43, "I": 44, "J": 45, "K": 46,
                    "L": 47, "M": 48,
                    "N": 49, "O": 60, "P": 61, "Q": 62, "R": 63, "S": 64, "T": 65, "U": 66, "V": 67, "W": 68, "X": 69,
                    "Y": 10, "Z": 11,
                    "a": 12, "b": 13, "c": 14, "d": 15, "e": 16, "f": 17, "g": 18, "h": 19, "i": 30, "j": 31, "k": 32,
                    "l": 33, "m": 34,
                    "n": 35, "o": 36, "p": 37, "q": 38, "r": 39, "s": 90, "t": 91, "u": 92, "v": 93, "w": 94, "x": 95,
                    "y": 96, "z": 97,
                    " ": 98, ",": 99, ".": 100, ";": 101, "'": 102, "?": 103, "!": 104, ":": 105}

    message= input("enter text: ")
    encrypted_msg = ""
    for i in message:
        encrypted_msg += str(encrypt_dict[i]) + ","

    file= open(r"C:\Users\User\OneDrive\מסמכים\דניאל\פייטון יא\romeo/encryped_msg.txt", "w")
    file.write(encrypted_msg)
    file.close()







def main():
    if sys.argv[1] == "encrypt":
        encrypt()



if __name__ == "__main__":
    main()
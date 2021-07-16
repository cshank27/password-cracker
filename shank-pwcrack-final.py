#!/usr/bin/env python3

#Clayton Shank

import time
import sys
import hashlib

#Dictionary attack
def dictionary_attack(pass_input):
    counter = 1

    #insert hash and dictionary file
    # passInput = input('Enter the MD5 hash: ')
    passfile = input('Enter the dictionary file name:')

    #trys to open password file
    try:
        passfile = open(passfile, "r")
    except:
        print('\nFile not found')
        sys.exit(1)
    #for loop to strip and decrypt md5 start timer
    #start timer for pw calculation
    start = time.time()
    for password in passfile:
        plain_pwd = password.strip()
        guess = hashlib.md5(plain_pwd.encode()).hexdigest()
        print(f"Trying password {counter}: {plain_pwd}")

        #adds counter every try
        counter += 1

        #found password and prints pw and time taken
        if guess == pass_input:
            print(f"\n[+] Password Found. \nPassword is: {password}")
            print('time: ' + str((time.time() - start)) + ' sec')
            break

def hashWithMethod(method, value):
    
    #encoding of hash
    if (method == "md5"):
        v = value.encode("utf-8")
        h = hashlib.md5(v).hexdigest()
        #print(value + " (" + str(len(value)) + "): " + h)
        return h
    raise ValueError('Unknown hash method "' + method + '"')

#nested for loop for 6 character password in bytes
def bruteforce(pass_input):
    method = "md5"
    curr = ""
    start = time.time()

    for byte1 in range(0,256):
        curr = str(chr(byte1))
        if (hashWithMethod(method, curr) == pass_input):
            print("Found: " + curr)
            print('time: ' + str((time.time() - start)) + ' sec')
            break
        for byte2 in range(0,256):
            curr = str(chr(byte1)) + str(chr(byte2))
            print(curr)
            if (hashWithMethod(method, curr) == pass_input):
                print("Found: " + curr)
                print('time: ' + str((time.time() - start)) + ' sec')
                break
        #     for byte3 in range(0,256):
        #         curr = str(chr(byte1)) + str(chr(byte2)) + str(chr(byte3))
        #         if (hashWithMethod(method, curr) == pass_input):
        #             print("Found: " + curr)
        #             print('time: ' + str((time.time() - start)) + ' sec')
        #             break
        #         # for byte4 in range(0, 256):
                #     curr = str(chr(byte1)) + str(chr(byte2)) + str(chr(byte3)) + str(chr(byte4))
                #     if (hashWithMethod(method, curr) == pass_input):
                #         print("Found: " + curr)
                #         print('time: ' + str((time.time() - start)) + ' sec')
                #         break
                #     for byte5 in range(0,256):
                #         curr = str(chr(byte1)) + str(chr(byte2)) + str(chr(byte3)) + str(chr(byte4)) + str(chr(byte5))
                #         if (hashWithMethod(method, curr) == pass_input):
                #             print("Found: " + curr)
                #             print('time: ' + str((time.time() - start)) + ' sec')
                #             break
                #         for byte6 in range(0,256):
                #             curr = str(chr(byte1)) + str(chr(byte2)) + str(chr(byte3)) + str(chr(byte4)) + str(chr(byte5)) + str(chr(byte6))
                #             if (hashWithMethod(method, curr) == pass_input):
                #                 print("Found: " + curr)
                #                 print('time: ' + str((time.time() - start)) + ' sec')
                #                 break
                                

def menu_selection():
    pass_input = input('Enter the MD5 hash: ')
    choice ='0'
    while choice =='0':
        print("Main Choice: Choose 1 of 2 choices")
        print("Choose 1 for Dictionary Crack")
        print("Choose 2 for Brute Force Crack")

        choice = input ("Please make a choice: ")

        if choice == "2":
            bruteforce(pass_input)
        elif choice == "1":
            dictionary_attack(pass_input)
        else:
            print("I don't understand your choice.")

if __name__ == "__main__":
    #menu selection
    menu_selection()

# password-cracker
dictionary and brute force password cracker for unsalted md5 hashes
Write a basic password cracking program using Python.  Your program should support brute force and dictionary cracking methods. 

This project will be restricted to unsalted md5 hashes.

You may only import 'hashlib', 'sys' and 'time' libraries.

Dictionary method - Your program should prompt the user for a dictionary file that contains possible passwords and the md5 hash of the password to be cracked.  Your program should then iterate through the dictionary file, hash each word and compare to the hash of the password.  When you have a match, you have cracked the password. I will test your program using a common dictionary list and random md5 hash of one of the words in the list.

Brute Force method - You program should accept a password hash or a file containing a password hash as input.  You should then develop a method for iterating through every possible combination, hashing each and comparing to the user provided password hash.  When the hashes mach, you've cracked the password.  Given the processing time required to brute force complex passwords, I will test your code on passwords shorter than 6 characters. 

Extra grading consideration will be given to students who implement functionality to crack complex passwords (upper case, lower case, special characters, and mangling).

The following items must be submitted to receive full credit for this project:
1) A brief explanation of your approach to this project
2) Commented code (.py file)

For both methods, your program should output to screen the cracked password, the time it took to crack the password and the number of passwords attempted.


#Clayton Shank


import time
import sys
import hashlib
#select dictionary, bruteforce, none exit

#Dictionary attack

counter = 1

#insert hash and dictionary file
passInput = raw_input('Enter the MD5 hash: ')
passfile = raw_input('Enter the dictionary file name:')

#trys to open password file
try:
    passfile = open(passfile, "r")
except:
    print '\nFile not found'
    quit()
#for loop to strip and decrypt mdf
for password in passfile:
    filemd5 = md5.new(password.strip()).hexdigest()
    print "Trying password %d: %s " % (counter, password.strip())

#adds counter every try
    counter += 1

#found password and prints
    if passInput == filemd5:
        print "\n[+] Password Found. \nPassword is: %s" % password


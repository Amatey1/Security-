# this is the library for hashing 
import hashlib
import random
import string 
# taking a clue from the user 
value = input ("Enter your text \n")

# hashing the string 
# converting the hash into characters 
# converting the characters to hexadecimal 

string = hashlib.sha256(value.encode('ascii')).hexdigest()

print(string)
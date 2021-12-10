# this is the library for hashing 
import hashlib
import random
import string 
# taking a clue from the user 
value = input ("Enter your text \n")

# hashing the string 
# converting the hash into characters 
# converting the characters to hexadecimal 

 
Salt = value.join((random.choice(string.ascii_letters)for x in range(5)))
value = hashlib.sha256(Salt.encode('ascii')).hexdigest()

print(value)
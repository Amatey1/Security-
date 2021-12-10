import math
import random
import rsa
# creating a public key
p = 53
q = 59

n = p*q



# Public key e

e = 2
phi = (p-1) * (q-1)
print ('phi is', phi)

#
while e < phi :
    if math.gcd(e,phi) == 1 :
        break
    else :
        e = e+1


k = 3

# The private key .
d = ((k*phi) + 1)/e


# Number to be encrypted
data = 12

print("Data to be encrpted:" + str(data))

enc_data = (data**e) % n

print("Encrypted message: " + str(enc_data))

print("Decrypted message: " + str(data))


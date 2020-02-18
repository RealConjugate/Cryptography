# RSA Encryption

import math
from random import randrange


# This is a complete prime number checker
def ModifiedPrimeCheck(x):
    sqrtInt = math.floor(math.sqrt(float(x))) + 1
    i = 2
    factors = 0
    while i < sqrtInt and factors == 0:
        if (x/i).is_integer():
            factors = factors + 1
            i = i+1
        else:
            i = i+1
    if factors == 0 and x > 1:
        return "prime"
    else:
        return "not prime"
    
            
def StartUI():
    print("1. Generate Key")
    print("2. Encrypt")
    print("3. Decrypt")
    select = input("Enter 1, 2 or 3. ")
    if select == "1":
        print("Please wait...")
        GenerateUI()
    elif select == "2":
        EncryptUI()
    elif select == "3":
        DecryptUI()
    else:
        StartUI()
        
    
def GenerateUI():
    lowerBound = 30
    upperBound = 200
    primes = [] # List containing the 2 primes
    while len(primes) < 2:
        num = randrange(lowerBound,upperBound)
        isPrime = ModifiedPrimeCheck(num)
        if isPrime == "prime":
            primes.append(num)

    p = primes[0]
    q = primes[1]
    n = p*q # n is released as part of the public key; p and q are secret
    L = int(lcm(p-1,q-1)) # L is secret
    e = L
    while gcd(e,L) != 1: # Choose e strictly between 1 and L coprime to L
        e = randrange(2,L)
    # e is released as part of the public key
    d = 0
    while (d*e) % L != 1:
        d = d + 1
    print("")
    print("Public Key")
    print("n=" + str(n))
    print("e=" + str(e))
    print("")
    print("Private Key")
    print("d=" + str(d))

    print("")
    StartUI()
        

def EncryptUI():
    a = 10 # This is just adding character corresponding ints to a list [10,11,12,13,...,85]
    charInts = []
    while a <= 85:
        charInts.append(a)
        a = a + 1

    chars = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','!','?','=','-','+',',','.',' ',':',';','@','<','>']
    
    n = int(input("Enter n from your public key."))
    e = int(input("Enter e from your public key."))
    
    plaintext = input("Enter your plaintext to encrypt. Only A-Z, a-z, 0-9, spaces and !?=-+,.:;@<> characters are permitted.")
    
    i = 0 # i is the index, starting from 0 not 1
    ciphertext = ""
    invalid = False
    while i <= len(plaintext) - 1 and invalid == False:
        if plaintext[i] in chars:
            m = charInts[chars.index(plaintext[i])]
            if i == 0:
                ciphertext = str(EncryptFunct(m,n,e))
            else:
                ciphertext = ciphertext + " " + str(EncryptFunct(m,n,e))
            i = i + 1
        else:
            invalid = False
            print("Your plaintext contains invalid characters. Please try again.")
            print("")
            EncryptUI()
    print(ciphertext)
    print("")
    StartUI()
    # Output a string that the user can then copy and paste to the other person


def DecryptUI(): # m = c^d mod n
    n = int(input("Enter n from your public key."))
    d = int(input("Enter d from your private key."))
    # can add testing for validity of cipherVar
    cipherVar = input("Enter the ciphertext to decrypt.") # now turn it into a list
    cipherVar = cipherVar + " " # Add space at the end
    cipherList = []
    
    i = 0 # index of position through cipher variable (note cipherVar can't start with a space)
    lastSpaceIndex = -1
    string = ""
    while i <= (len(cipherVar)-1): # Slices variable into list
        if cipherVar[i] == " ":
            for j in range((lastSpaceIndex + 1), (i)):
                string = string + cipherVar[j]
            cipherList.append(int(string))
            string = ""
            lastSpaceIndex = i
            i = i + 1
        else:
            i = i + 1

    chars = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','!','?','=','-','+',',','.',' ',':',';','@','<','>']
    a = 10
    charInts = []
    while a <= 85:
        charInts.append(a)
        a = a + 1
    
    decryptedText = ""
    k = 0
    while k <= (len(cipherList)-1):
        m = DecryptFunct(n,cipherList[k],d)
        bar = chars[charInts.index(m)]
        decryptedText = decryptedText + bar
        bar = ""
        k = k+1
    print("")
    print("DECRYPTED TEXT:")
    print("")
    print(decryptedText) # Prints decrypted text
    print("")
    StartUI()
    
    


        

def EncryptFunct(m,n,e):
    c = (m**e) % n
    return c

def DecryptFunct(n,c,d):
    m = (c**d) % n
    return m
    

def gcd(a,b):
    while b > 0:
        a, b = b, a%b
    return a
            
def lcm(x,y):
    return (x*y)/gcd(x,y)

    
    
    
StartUI()    

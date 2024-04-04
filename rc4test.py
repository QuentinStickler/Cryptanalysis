___doc___ = '''

File for testing the RC4 algorithm and also trying to crack it

'''

###Here, we initialize our S-Box with values from 0-255 and our T-Box, which just contains repeated values of our given key 256 times
def initialize(plaintext):
    S = [0] * 256
    key = "Supersicherer Key"            ###Enter your key here
    asciikey = []
    T = [0] * 256

    for c in key:                   ###Create ascii list from key 
        asciikey.append(ord(c))
    keylength = len(asciikey)


    for x in range(256):            ###Initilaze S-Box and T-Box
        S[x] = x
        T[x] = asciikey[x % keylength]

    permutation(S,T,plaintext)

###Here, we use our initialized S-Box and T-Box to permutate the S-Box
###It will then include all values from 0-256 still, but now in a (pseudo-)random order dependent on our given key
def permutation(S,T,plaintext):
    j = 0
    for i in range(256):
        j = (j + S[i] + T[i]) % 256
        currentvalue = S[i]
        S[i] = S[j]
        S[j] = currentvalue
    generatestream(S, plaintext)


def generatestream(S, plaintext):
    i = 0
    j = 0

    asciiplaintext = []
    for c in plaintext:                   
        asciiplaintext.append(ord(c))
    plaintextlength = len(asciiplaintext)
    keystream = []

    for x in range(plaintextlength):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        currentValue = S[i]
        S[i] = S[j]
        S[j] = currentValue
        t = (S[i] + S[j]) % 256
        keystream.append(S[t])

    ciphertext = encrypt(asciiplaintext, keystream)
    decrypt(ciphertext, keystream)

def encrypt(asciiplaintext, keystream):

    encryptedlist = []
    for x,y in zip(asciiplaintext,keystream):
        encryptedlist.append(chr(x^y))
    return encryptedlist

def decrypt(ciphertext, keystream):

    decryptedlist = []
    for x,y in zip(ciphertext,keystream):
        decryptedlist.append(chr(ord(x)^y))
    result = ""
    for value in decryptedlist:
        result += value
    print(result)
    return result

plaintext = "Plaintext"
initialize(plaintext)

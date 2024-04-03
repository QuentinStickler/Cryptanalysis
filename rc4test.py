___doc___ = '''

File for testing the RC4 algorithm and also trying to crack it

'''

###Here, we initialize our S-Box with values from 0-255 and our T-Box, which just contains repeated values of our given key 256 times
def initialize():
    S = [0] * 256
    key = "I AM THE KEY"            ###Enter your key here
    asciikey = []
    T = [0] * 256

    for c in key:                   ###Create ascii list from key 
        asciikey.append(ord(c))
    keylength = len(asciikey)


    for x in range(256):            ###Initilaze S-Box and T-Box
        S[x] = x
        T[x] = asciikey[x % keylength]

    permutation(S,T)

###Here, we use our initialized S-Box and T-Box to permutate the S-Box
###It will then include all values from 0-256 still, but now in a (pseudo-)random order dependent on our given key
def permutation(S,T):
    j = 0
    for i in range(256):
        j = (j + S[i] + T[i]) % 256
        currentvalue = S[i]
        S[i] = S[j]
        S[j] = currentvalue


def generatestream():
    return None

initialize()

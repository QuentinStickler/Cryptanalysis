from scipy.stats import binom

___doc___ = '''

File for testing the RC4-algorithm

'''
#region SecondImplmentation
def initialize(key):
    #Initialize S-box with values 0-255 and kbox with repeated key values
    sbox = [0] * 256
    kbox = [0] * 256
    for x in range(256):
        sbox[x] = x
        kbox[x] = key[x % len(key)]
        
    j = 0
    for i in range(256):
        #Permutate s-box with the given key
        j = (j + sbox[i] + kbox[i]) % 256

        #Swap sbox[i] and sbox[j]
        tmp = sbox[i]
        sbox[i] = sbox[j]
        sbox[j] = tmp
    return sbox
    

def stream_generation(sbox, text):
    keystream = []
    i = 0
    j = 0
    #Generate random keystream with length of plaintext
    for x in range(len(text)):
        i = (1 + i) % 256
        j = (sbox[i] + j) % 256
        
        #Swap sbox[i] and sbox[j]
        tmp = sbox[j]
        sbox[j] = sbox[i]
        sbox[i] = tmp

        result = sbox[i] + sbox[j] % 256
        
        keystream.append(sbox[result])    
    return keystream    


def encrypt(text, key):
    text = [ord(char) for char in text]
    
    sbox = initialize(key)
    key_stream = stream_generation(sbox, text)
    
    ciphertext = ''
    i = 0
    for char in text:
        #Plaintext in Hex for better visualization
        enc = str(hex(char ^ key_stream[i])).upper()
        ciphertext += (enc)
        i += 1 
    return ciphertext
    

def decrypt(ciphertext, key):
    #Crop out the "0X" from the Hex presentation
    ciphertext = ciphertext.split('0X')[1:]
    ciphertext = [int('0x' + c.lower(), 0) for c in ciphertext]
    
    sbox = initialize(key)
    key_stream = stream_generation(sbox, ciphertext)
    
    plaintext = ''
    i = 0
    for char in ciphertext:
        dec = str(chr(char ^ key_stream[i]))
        plaintext += dec
        i += 1
    
    return plaintext


if __name__ == '__main__':
    mode = input('Do you want to encrypt ("E") or Decrypt ("D")?: ').upper()
    if mode == 'E':
        plaintext = input('Please enter the text you want to encrypt: ')
        key = input('Please enter you key: ')
        key = [ord(char) for char in key]
        result = encrypt(plaintext, key)
        print('Result: ')
        print(result)
    elif mode == 'D': 
        ciphertext = input('Please enter the text you want to decrypt: ')
        key = input('Pleas enter your key: ')
        key = [ord(char) for char in key]
        result = decrypt(ciphertext, key)
        print(f'Result: {result}')
    else:
        print('Error in input - try again.')
#endregion

#region Testing Ground 

def testinitialize(plaintext, key):
    S = [0] * 256
    asciikey = []
    T = [0] * 256

    for c in key:                   ###Create ascii list from key 
        asciikey.append(ord(c))
    keylength = len(asciikey)


    for x in range(256):            ###Initilaze sbox and T-Box
        S[x] = x
        T[x] = asciikey[x % keylength]

    # result = [value for value in T]
    # print(result)

    return testpermutation(S,T,plaintext)

def testpermutation(S,T,plaintext):
    j = 0
    for i in range(256):
        j = (j + S[i] + T[i]) % 256
        currentvalue = S[i]
        S[i] = S[j]
        S[j] = currentvalue
    # result = [value for value in S]
    # print(result)
    return testgeneratestream(S, plaintext)

def testgeneratestream(S, plaintext):
    i = 0
    j = 0

    asciiplaintext = []
    for c in plaintext:                   
        asciiplaintext.append(ord(c))
    plaintextlength = len(asciiplaintext)
    keystream = []

    for x in range(plaintextlength):
        # print(f"i:{i}")
        # print(f"j:{j}")
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        # print(f"i:{i}")
        # print(f"j:{j}")
        # print(f"S[i] = {S[i]}")
        # print(f"S[j] = {S[j]}")
        currentValue = S[i]
        S[i] = S[j]
        S[j] = currentValue
        t = (S[i] + S[j]) % 256
        # print(f"t = {t}")
        # print("#########")
        keystream.append(S[t])
    
    # for v in keystream:
    #     print(v)
    return asciiplaintext, keystream

def testencrypt(asciiplaintext, keystream):
    encryptedlist = []
    for x,y in zip(asciiplaintext,keystream):
        encryptedlist.append(chr(ord(str(x))^y))

    result = ""
    for val in encryptedlist:
        result += val
    print(result)

def maintest():
    plaintext = "TestText"
    key= "TestKey"
    asciiplaintext, keystream = testinitialize(plaintext, key)
    testencrypt(asciiplaintext, keystream)


def testprobability():
    #Win percentage
    success_probability = 0.05
    #Win probability
    target_probability = 0.95
    num_trials = 1

    #Go through the IVs
    while True:
        cumulative_probability = 1 - binom.cdf(0, num_trials, success_probability)
        if cumulative_probability >= target_probability:
            break
        num_trials += 1

    print(f"Number of needed IVs to recover K3 with a probability of {target_probability} is: ", num_trials)

#Probability of recovering K3 after num tries
def test():
    success_probability = 0.05
    num_ivs = 60
    probability = 1 - binom.cdf(0, num_ivs, success_probability)
    print(f"Probability of recovering K3 after {num_ivs} tries: ", probability)

def testprobabilityofspecificivs():

    # Anzahl der abgefangenen Pakete
    n = 5000000

    # Wahrscheinlichkeit, einen IV der Form (3, 255, V) in einem einzelnen Paket zu erhalten
    p = 1 / (256**2)

    # Berechne die Wahrscheinlichkeit, mindestens 60 IVs zu erhalten
    probability_at_least_60 = binom.sf(59, n, p)

    print("Die Wahrscheinlichkeit, mindestens 60 IVs zu erhalten, beträgt:", probability_at_least_60)


def recoverkeystreambyte(ivb1, ivb2, ivb3, ivb4, wantedbyte):
    sbox = [0] * 256
    for i in range(255):
        sbox[i] = i
    key = [ivb1,ivb2,ivb3,ivb4]
    i = 0
    j = 0
    for x in range(wantedbyte):
        j = (j + sbox[i] + key[i]) % 256
        s_j = sbox[j]
        sbox[j] = sbox[i]
        sbox[i] = s_j
        # print(f"i: {i}")
        # print(f"j: {j}")
        # for x in range(wantedbyte):
        #     print(sbox[x])
        # print("-------------")
        i += 1

    t = sbox[1] + sbox[sbox[1]]
    if(t == wantedbyte):
        print("IV works.")
    else: print("IV doesn't work.")


#recoverkeystreambyte(4,255,123,69, 4)
#endregion
from scipy.stats import binom

___doc___ = '''

File for testing the RC4-algorithm and certain probabilities for catching IVs 

'''
#region Implmentation
def initialize(key):
    #Initialize S-box with values 0-255 and kbox with repeated key values
    sbox = [0] * 256
    kbox = [0] * 256
    for x in range(256):
        sbox[x] = x
        kbox[x] = key[x % len(key)]
        
    j = 0
    for i in range(256):
        #Permutate s-box based on the given key
        j = (j + sbox[i] + kbox[i]) % 256

        #Swap entries in sbox[i] and sbox[j]
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

        result = (sbox[i] + sbox[j]) % 256
        
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
#How many IVs are needed given a certain success_probability and desired win probability
def testprobability():
    #Win percentage
    success_probability = 0.05
    #Win probability. 0.95 means how many IVs will we need if we want to recover a key byte with a chance of 95%
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
def testrecovery():
    success_probability = 0.05
    num_ivs = 60
    probability = 1 - binom.cdf(0, num_ivs, success_probability)
    print(f"Probability of recovering K3 after {num_ivs} tries: ", probability)

def testprobabilityofspecificivs():

    # Number of caught packets
    n = 5000000
    # Probability to get certain IV 
    p = 1 / (256**2)
    # Probability of getting at least 60 IVs
    probability_at_least_60 = binom.sf(59, n, p)

    print("Probability to obtain at least 60 Ivs:", probability_at_least_60)


#Test if given IV is useful for K3
def recoverkeystreambyte(ivb1, ivb2, ivb3):
    sbox = [0] * 256
    for i in range(255):
        sbox[i] = i
    key = [ivb1,ivb2,ivb3]
    i = 0
    j = 0
    for x in range(3):
        j = (j + sbox[i] + key[i]) % 256
        s_j = sbox[j]
        sbox[j] = sbox[i]
        sbox[i] = s_j
        i += 1

    t = sbox[1] + sbox[sbox[1]]
    if(t == 3):
        print(f"IV {ivb1, ivb2, ivb3} works.")
    #else: print(f"IV {ivb1, ivb2, ivb3} doesn't work.")

#Decomment to find useful IVs for K3
# for i in range(255):
#     for j in range(255):
#         recoverkeystreambyte(i,253,j)
#endregion
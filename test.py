import os
import random
random.seed(1984)

files = os.listdir()

s = 'N<Пуcwl\neр1AxVtbюРpж3fdУп?qёЧ ьunrО)7цтh–Bхэ(=a6НC—об5Десvo>гфйF:д\tшк/ач9_’|gз8ыщ]+s"m[0TSВ‘,ияi4нл2мв.-'
original = list(s)
secret = original.copy()
random.shuffle(secret)

d1 = {original[i]: secret[i] for i in range(len(original))}
d2 = {secret[i]: original[i] for i in range(len(original))}

def encrypt(s, d):
    result = ''
    for i in s:
        if i in d:
            result += d[i]
        else:
            result += i
    return result


with open('midterm.txt', encoding='utf-8') as fid:
    r = fid.read()

with open('midterm_encrypted.txt', 'w', encoding='utf-8') as fid:
    fid.write(encrypt(r, d1))

print("Encryption complete. Encrypted file saved as 'midterm_encrypted.txt'.")
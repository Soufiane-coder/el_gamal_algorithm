import random
from math import gcd
a = random.randint(2, 10)

# For key generation i.e. large random number


def gen_key(q):
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)
    return key


def encryption(msg, q, h, g):
    ct = []
    k = gen_key(q)
    s = pow(h, k, q)
    p = pow(g, k, q)
    for i in range(0, len(msg)):
        ct.append(msg[i])
    print("g^k used= ", p)
    print("g^ak used= ", s)
    for i in range(0, len(ct)):
        ct[i] = s*ord(ct[i])
    return ct, p
# For decryption


def decryption(ct, p, key, q):
    pt = []
    h = pow(p, key, q)
    for i in range(0, len(ct)):
        pt.append(chr(int(ct[i] / h)))
    return pt


msg = input("Enter message.")
q = random.randint(pow(10, 20), pow(10, 50))
g = random.randint(2, q)
key = gen_key(q)
h = pow(g, key, q)

print("g used=", g)
print("g^a used=", h)

ct, p = encryption(msg, q, h, g)
print("Original Message=", msg)
print("Encrypted Maessage=", ct)

pt = decryption(ct, p, key, q)
d_msg = ''.join(pt)
print("Decryted Message=", d_msg)

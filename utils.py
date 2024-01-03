from sympy import factorint
from random import randint
from sympy import isprime

def find_primitive_root(p):
    factors = factorint(p - 1)  # Factorize p - 1

    def is_primitive(g):
        for q in factors.keys():
            # if it equel to one It means there
            # is a number g such that g^(that numer) = 1 mod(p)
            # rather than phi so phi(p) != ord(p) so it's not primitive root
            if pow(g, (p - 1) // q, p) == 1:
                return False
        return True

    for g in range(2, p):
        if is_primitive(g):
            return g

    return None  # No primitive root found

def get_large_prime():
    num = randint(pow(10, 20), pow(10, 50))
    while not isprime(num):
        num = randint(pow(10, 20), pow(10, 50))
    return num
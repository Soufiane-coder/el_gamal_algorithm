from random import randint
from utils import find_primitive_root, get_large_prime


def generate_keys():
    # p = randint(pow(10, 2), pow(10, 10))
    # g = randint(2, p - 1)  # not secure

    p = get_large_prime()  # Replace with a large prime number
    g = find_primitive_root(p)   # Replace with a primitive root modulo p

    a = randint(2, p - 2)  # Private key

    A = pow(g, a, p)  # Public key
    return p, g, a, A


def encryption(m, p, g, A):
    x = randint(2, p - 1)
    c1 = pow(g, x, p)
    c2 = (m * pow(A, x, p)) % p
    return c1, c2


def decryption(c1, c2, a, p):
    x = pow(c1, a, p)
    m = (pow(x, -1, p) * c2) % p
    return m


def main():
    p, g, key, A = generate_keys()
    c1, c2 = encryption(ord('s'), p, g, A)

    m = decryption(c1, c2, key, p)

    # for a in range(2, p - 1):
    #     if pow(g, a, p) == A:
    #         print('a found')
    #         print(chr(decryption(c1, c2, a, p)))

    print(f'message est : {chr(m)}')


if __name__ == '__main__':
    main()

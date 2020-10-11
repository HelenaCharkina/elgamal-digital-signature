from Algorithms import modexp
from GetHash import get_hash
from KeysGenerator import find_mutually_prime


def encrypt(keys, message):
    intHash = get_hash(message)

    k = find_mutually_prime(keys.p)
    print("k = ", k)

    r = modexp(keys.g, k, keys.p)
    print("r = ", r)

    l = modexp(k, -1, keys.p - 1) # мультипликативное обратное
    s = l * (intHash - keys.private_key * r) % (keys.p - 1)
    print("l = ", l)
    print("s = ", s)
    return r, s

def decrypt(keys, r, s, message):
    if not (r > 0 and r < keys.p):
        return False
    if not (s > 0 and s < keys.p - 1):
        return False
    intHash = get_hash(message)

    v1 = pow(keys.public_key, r, keys.p) % keys.p * pow(r, s, keys.p) % keys.p
    print("v1 = ", v1)

    v2 = pow(keys.g, intHash, keys.p)
    print("v2 = ", v2)

    return v1 == v2

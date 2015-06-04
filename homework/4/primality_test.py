import random

carmichael = [
    41041,
    62745,
    63973,
    75361,
    101101,
    126217,
    172081,
    188461,
    278545,
    340561,
    449065,
    552721,
    656601,
    658801,
    670033,
    748657,
    838201,
    852841,
    997633,
    1033669,
    1082809,
    1569457,
    1773289,
    2100901,
    2113921,
    2433601,
    2455921
]

# Unmodified Algorithm
def fermat(p, iterations):
    if p == 1:
        return False

    for i in range(0, iterations):
        a = random.randint(1, p - 1)

        if ((a ** p-1) % p) != 1:
            return False

    return True

# Unmodified Algorithm
def miller_rabin(p, iterations):
    if p < 2:
        return False

    if p != 2 and p % 2 == 0:
        return False

    s = p-1

    while s % 2 == 0:
        s = s / 2

    for i in range(0, iteration):
        a = random.randint(0, p - 1) + 1
        temp=s
        mod=(a ** temp) % p
        while (temp != p-1) and (mod != 1) and (mod != p-1):
            mod = (mod * mod) % p
            temp *= 2

        if (mod != p-1) and (temp % 2 == 0):
            return False

    return true

# Modified to step up until we find the smallest liar.
def fermat_lowest_witness(p):
    if p == 1:
        return 1

    for a in range(2, p - 1):
        if ((a ** (p-1)) % p) != 1:
           return a

def fermat_lowest_liar(p):
    if p == 1:
        return -1

    for a in range(2, p - 1):
        if ((a ** (p-1)) % p) == 1:
            return a

def fermat_test():
    print("Running Fermat Test:")
    for n in carmichael:
        r = fermat_lowest_witness(n)
        print("Found lowest witness for {}: {}".format(n, r))
        r = fermat_lowest_liar(n)
        print("Found lowest liar for {}: {}".format(n, r))

# Modified to step up until we find the smallest liar.
def miller_rabin(p):
    if p < 2:
        return -1

    if p != 2 and p % 2 == 0:
        return -1

    # compute m
    m = p - 1

    while m % 2 == 0:
        m = m / 2

    for a in range(2, p):
        x = (a ** m) % p
        if (x % p) == 1:
            return True

        temp = m
        while (temp != p-1) and (mod != 1) and (mod != p-1):
            mod = (mod * mod) % p
            temp *= 2

        if (mod != (p-1)) and ((temp % 2) == 0):
            return False

    return True

# Modified to step up until we find the smallest liar.
def miller_rabin_lowest_witness(p):
    if p < 2:
        return -1

    if p != 2 and p % 2 == 0:
        return -1

    # compute m
    m = p - 1

    while m % 2 == 0:
        m = m / 2

    for a in range(2, p):
        x = (a ** m) % p
        if (x % p) == 1:
            continue

        temp = m

        while (temp != p-1) and (x != 1) and (x != p-1):
            x = (x * x) % p
            temp *= 2

        if (x != (p-1)) and ((temp % 2) == 0):
            return a

    return -1

# Modified to step up until we find the smallest liar.
def miller_rabin_lowest_liar(p):
    if p < 2:
        return -1

    if p != 2 and p % 2 == 0:
        return -1

    # compute m
    m = p - 1

    while m % 2 == 0:
        m = m / 2

    for a in range(2, p):
        x = (a ** m) % p
        if (x % p) == 1:
            return a

        temp = m
        while (temp != p-1) and (x != 1) and (x != p-1):
            x = (x * x) % p
            temp *= 2

    return -1


def miller_rabin_test():
    print("Running Miller-Rabin Test:")
    for n in carmichael:
        r = miller_rabin_lowest_witness(n)
        print("Found lowest witness for {}: {}".format(n, r))
        r = miller_rabin_lowest_liar(n)
        print("Found lowest liar for {}: {}".format(n, r))

fermat_test()
print("-" * 20)
miller_rabin_test()

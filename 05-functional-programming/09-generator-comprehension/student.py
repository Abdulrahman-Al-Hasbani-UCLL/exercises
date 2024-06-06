def is_prime(n):
    if n < 2:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

def primes():
    n = 2
    while True:
        is_prime = True
        for x in range(2, n):
            if n % x == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 1
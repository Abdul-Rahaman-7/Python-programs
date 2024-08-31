def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            return False
    return True

def find_primes(a):
    p = []
    b = 2
    while len(p) < a:
        if is_prime(b):
            p.append(b)
        b += 1
    return p

a = int(input("enter the number of primes to find: "))
print("first", a, "primes are", find_primes(a))


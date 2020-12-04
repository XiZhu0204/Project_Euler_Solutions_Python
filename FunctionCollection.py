import math


def check_prime(x):
    # 1 and 0 are not prime, all even numbers are not prime
    if x == 1 or x == 0 or x % 2 == 0:
        return False
    # 2 is prime
    if x == 2:
        return True

    for i in range(3, math.ceil(math.sqrt(x)) + 1, 2):
        # increment by two, no need to check even factors
        if x % i == 0:
            return False

    # Done for loop, must be prime
    return True


def find_prime_factors(num):
    prime_array = []
    while num % 2 == 0:
        num /= 2
        prime_array.append(2)
    for i in range(3, int(num + 1) + 1, 2):
        while num % i == 0:
            num /= i
            prime_array.append(i)
    return prime_array

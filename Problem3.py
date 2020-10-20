# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# As numbers become large, their largest prime factor is generally less than its square root
import math


def checkPrime(x):
    # 1 and 0 are not prime, all even numbers are not prime
    if x == 1 or x == 0 or x % 2 == 0:
        return False
    # 2 is prime
    if x == 2:
        return True

    for i in range(3, math.ceil(math.sqrt(x)), 2):
        # increment by two, no need to check even factors
        if x % i == 0:
            return False
    # Done for loop, must be prime
    return True


number = 600851475143
largestPrime = 3

for k in range(3, math.ceil(math.sqrt(number)), 2):
    if number % k == 0 and checkPrime(k):
        largestPrime = k

print(largestPrime)

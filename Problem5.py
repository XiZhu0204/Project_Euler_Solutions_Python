# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# Find all common prime factors of numbers 1 - 20
from functionCollection import find_prime_factors

primeFactorArray = []

for x in range(2, 21):
    # create a 2D array of the prime factors of every number from 2 - 20
    primeFactorArray.append(find_prime_factors(x))

result = 1

for k in range(2, 20):
    maxOccurrence = 0
    for j in range(len(primeFactorArray)):
        occurrenceCount = 0
        for v in primeFactorArray[j]:
            if k == v:
                occurrenceCount += 1
        if occurrenceCount > maxOccurrence:
            maxOccurrence = occurrenceCount

    result = result * (k ** maxOccurrence)

print(result)

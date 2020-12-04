"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from functionCollection import check_prime


result = 0

for i in range(2000000):
    if check_prime(i):
        result += i

print(result)



"""
Note that using the implemented sieve of Eratosthenes in functionCollection is significantly slower

print(sum(find_primes_below(2000000)))

For the future, find out what makes it slower as the sieve should be faster than trial division
"""
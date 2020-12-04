# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# As numbers become large, their largest prime factor is generally less than its square root
import math
from functionCollection import check_prime


number = 600851475143
largestPrime = 3

for k in range(3, math.ceil(math.sqrt(number)), 2):
    if number % k == 0 and check_prime(k):
        largestPrime = k

print(largestPrime)

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

from FunctionCollection import check_prime

primeCount = 1
numberToCheck = 3

while True:
    if check_prime(numberToCheck):
        primeCount += 1

    if primeCount == 10001:
        print(numberToCheck)
        break

    numberToCheck += 2

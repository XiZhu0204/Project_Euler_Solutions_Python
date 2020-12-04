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

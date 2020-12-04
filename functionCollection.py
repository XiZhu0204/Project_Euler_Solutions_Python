import math


def check_prime(x):
    # 2 is prime
    if x == 2:
        return True
    # 1 and 0 are not prime, all even numbers are not prime
    if x == 1 or x == 0 or x % 2 == 0:
        return False

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


def read_file_to_1d_array(infile):
    tempstr = ""
    for i in infile:
        tempstr += i.replace("\n", "")
    return [x for x in tempstr]


def find_primes_below(max_num):
    # Initialize list to all zeros
    num_list = [0] * max_num
    for i in range(2, max_num):
        # Each index corresponds to the number it holds
        # 1 and 0 are not primes, exclude from list construction
        num_list[i] = i

    for k in range(2, max_num):
        # If entry is not zero, it is not a multiple of previous numbers, which means prime
        if num_list[k] != 0:
            for x in range(num_list[k]*2, max_num, num_list[k]):
                # Remove all multiples of the prime number
                num_list[x] = 0

    while 0 in num_list:
        num_list.remove(0)

    return num_list

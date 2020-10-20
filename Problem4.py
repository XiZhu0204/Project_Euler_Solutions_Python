# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# Start from 999 x 999 and check if palindromic

def check_palindrome(num):
    numArray = [char for char in str(x*y)]
    # the multiple of two 3-digit numbers is 6 digits long, therefore numArray has 6 entries
    for i in range(0, 3):
        negativeIndex = -(i+1)
        if numArray[i] != numArray[negativeIndex]:
            return False
    return True


PalindromeFound = False

for x in range(999, 900, -1):
    if PalindromeFound:
        break
    for y in range(999, 900, -1):
        if check_palindrome(x*y):
            print(x*y)
            PalindromeFound = True
            break


"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
We know that Pythagorean triplets can be constructed according to the formula:
Let m, n be positive integers such that m > n
then
a = 2mn
b = m^2 - n^2
c = m^2 + n^2
Since a + b + c = 1000
then 2mn + (m^2 - n^2) + (m^2 + n^2) = 1000
2mn + 2(m^2) = 1000
mn + m*m = 500
m(m+n) = 500
Now we find values m and n by guess and check
"""
finished = False

for n in range(500):
    for m in range(500):
        if m*(m+n) == 500:
            print((2*m*n)*(m*m - n*n)*(m*m + n*n))
            finished = True
            break
        if finished:
            break

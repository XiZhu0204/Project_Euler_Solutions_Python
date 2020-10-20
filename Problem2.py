# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

result = 0
x = 1
y = 1

while True:
    temp = y
    y += x
    x = temp

    if y >= 4000000:
        print(result)
        break
    elif y % 2 == 0:
        result += y
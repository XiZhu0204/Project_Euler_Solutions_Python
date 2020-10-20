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

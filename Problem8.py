"""
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

7316717... (see input file)

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?
"""

from FunctionCollection import read_file_to_1d_array

inData = open("Problem8_Input", "r")

numArray = read_file_to_1d_array(inData)
inData.close()

for i in range(len(numArray)):
    numArray[i] = int(numArray[i])

greatestProduct = 0

for k in range(0, (len(numArray) - 13)):
    product = 1
    if numArray[k] != 0:
        for x in range(13):
            product *= numArray[k + x]

    if product > greatestProduct:
        greatestProduct = product

print(greatestProduct)

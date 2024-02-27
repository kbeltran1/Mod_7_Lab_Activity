import math
def list_multipy(numbers):
    product = 1
    for number in numbers:
        product = product * number
        return product
list1 = [5, 2, 7, -1]

print(math.prod(list1))

# Kelly Beltran
# 02-26-24
# Problem 3: Takes the numbers from a list and multiplies them by one
# another to get a product
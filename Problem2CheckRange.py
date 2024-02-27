def test_range(n):
    if n in range(1,10):
        print("%s is in the range" % str(n))
    else:
        print("The number is outside the given range")
test = int(input("Enter any number: "))

test_range(test)

# Kelly Beltran
# 02-26-24
# Problem 2: you enter a number and program responds whether number is
# or is not in the given range
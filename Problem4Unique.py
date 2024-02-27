def unique_list(ul):
    x = []

    for a in ul:
        if a not in x:
            x.append(a)
    return x

print(unique_list([1, 3, 3, 3, 6, 2, 3, 5]))

# Kelly Beltran
# 02-26-24
# Problem 4: I list is looked at and all repeated numbers are taken out

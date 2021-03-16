def filter_even(*num, li=None):
    if li is None:
        li = []
    for num in num:
        if num%2 == 0:
            li.append(num)

    return li

print(filter_even(1, 2, 3, 4, 5))
print(filter_even(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
def num_to_list(num):
    li = []
    base = 10**(len(str(num)) - 1)
    for s in str(num):
        li.append(int(s) * base)
        base = int(base / 10)
    return li

li1 = num_to_list(54321)
li2 = num_to_list(1004)

print(li1)
print(li2)
number = 36
count = 0
if number % 10 == 3 or number % 10 == 6 or number % 10 == 9:
    count += 1
if number // 10 % 10 == 3 or number // 10 % 10 == 6 or number // 10 % 10 == 9:
    count += 1

print(count)

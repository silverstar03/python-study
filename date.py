def print_day(day):
    print_day=["화", "수", "목", "금", "토", "일", "월"]
    print(print_day[day%7],"요일")

a = print_day(13)

for i in range(1,32):
    print_day(i)
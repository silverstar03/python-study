# clap = "짝"
# for i in range(1,100):
#     num = i
#     if i%10==3 or i%10==6 or i%10==9:
#         print(clap, end="")
#         num = num//10
#         if num%10==3 or num%10==6 or num%10==9:
#             print(clap)
#     else:
#         print(i)


for i in range(1, 100+1):
    result = ""
    num = str(i)
    is369 = False
    for n in num:
        if '3' in num or '6' in num or '9' in num:
            result += "짝"
            is369 = True

    if is369 == True:
        print(result)
    else:
        print(num)

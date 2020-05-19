# for 연습
# 구구단 7단 출력하기
# for i in range(1, 10): #주어진 숫자가 눈에 보이게 함(10을 9+1로)
#     print(7, "x", i, "=", 7*i)

#구구단 2~9단까지 출력하기
for dan in range(2,10):
    print("-"*10)
    for i in range(1,10):
        print(dan, "x", i, "=", dan*i)
# for 연습
# 구구단 7단 출력하기
# for i in range(1, 10): #주어진 숫자가 눈에 보이게 함(10을 9+1로)
#     print(7, "x", i, "=", 7*i)

#구구단 2~9단까지 출력하기
# for dan in range(2,10):
#     print("-"*10)
#     for i in range(1,10):
#         print(dan, "x", i, "=", dan*i)

#N자리수의 각 자리 숫자합 출력하기
num = input("숫자를 입력하세요 : ")
sum = 0
for ch in num:
    sum += int(ch)

#for i in range(0, len(num)):
#    n = num[i]
#    sum += int(n)

#num에 더하자
#sum 출력하자
print(sum)

#369 게임
#전화번호부 만들고, 이름으로 검색하기
#주차요금 계산하기, 최초 30분 2800원, 10분당 1000원, 2500원 넘을 수 없음
#야구게임
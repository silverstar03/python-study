# num = 1
# while num <= 10:
#     print(num, end=" ")
#     num += 1
# print()
#
# while True:
#     val = input()
#     if val == "quit":
#         # 반복문 탈출
#         break
# print(val)
from functools import reduce

a = 1
b = 10
c = 2

# 1, 2, 3, ..., 8, 9
print(range(a, b))

# 1, 3, 5, 7, 9
print(range(a, b, c))

# for(int i=1;i<11;i++) {
#     sysout(i)
# }

# for i in range(1, 11):
#     print(i, end=" ")
# print()
#
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     print(i, end=" ")
# print()

# for i in range(1, 11, 3):
#     print(i, end=" ")
# print()

# mylist = [1, 2, 3, 4, 5]
# mylist = ['a', 'b', 'c']
# for i in mylist:
#     print(i, end=" ")
# print()

# myset = {"Hello", "World"}
# # 순서 주의! (set에 정의된 순서대로 출력 안될 수 있음)
# for word in myset:
#     print(word, end=" ")
# print()

result = [i * 2 for i in range(2, 20, 2)]
result = [i for i in range(2, 20, 2)]
result = [(i % 2 == 0) for i in range(1, 11)]
print("result", result)

mylist = [1, 2, 3, 4]
after_multiply = [i * i for i in mylist]
print("after_multiply", after_multiply)

numbers = [1, 2, 3, 4, 5]
new_list = [n**2 for n in numbers if n % 2 == 0]
print("new_list", new_list)


names = ["김철수", "신구", "이철수", "박철수", "김영희", "박철"]

# Q) 리스트 컴프리헨션써서 김씨만 거르기 (startsWith 메소드 사용)
name = "김철수"
# name.startsWith("김")

# Q) 리스트 컴프리헨션써서 이름이 두 자인 사람만 거르기 (len 함수 사용)
len(name) # ==> 3

# Q) 김씨 거르기, 이름 두자 거르기를 for 문을 이용해서 해보기
filtered = []
filtered.append("김철수")
# for ...

kim = []
for n in names:
    if n.startswith("김"):
        kim.append(n)
print(kim)

result = [n for n in names if n.startswith("김")]
print(result)

two = []
for n in names:
    if len(n) == 2:
        two.append(n)
print(two)

result = [n for n in names if len(n) == 2]
print(result)

# result = *(n for n in names if len(n) == 2),
# print(result)
#
# result = {n for n in names if len(n) == 2}
# print(result)


for i in range(2, 10):
    g = [i * j for j in range(1, 10)]
    # print(g)

result = [x for x in [n for n in names if len(n) == 2] if x.startswith("신")]
print(result)






a = 1 + 3

# 제곱
a = 2 ** 3
print(a) # 8

# 나누기 연산 결과로 소수가 반환됨 주의
a = 3 / 2
print(a)

# 나머지 연산
a = 3 % 2
print(a)
a = 5 % 3
print(a)

a += 1
a *= 2
# a++

# 논리 연산자
print(True and False)
print(False or False)
print(not True)
print(not False)
print(not 1 != 1)

# in, not in (Membership Operators)
# 포함 관계를 조사하는 연산자
li = [1, 2, 3, 4]
print(1 in li)  # 1이 포함되어 있으므로 True
print(5 in li)
print(5 not in li)  # 1이 포함되어 있지 않으므로 True
print(not (5 in li))  # 위와 같은 결과

print("a" in "asdf")
print("Hell" in "Hello")

dic = {"name": "John"}
print("name" in dic)  # 속성이 존재하므로 True
print("age" in dic)





# 순서 X
# 중복으로 저장 X
# 합집합, 교집합, 차집합같은 집합 연산 가능

s1 = {1, 2, 3}
s2 = {2, 3, 4, 4}
# s3 = {} # 타입? => 딕셔너리
s3 = set()

# print(s1[0])
print(s1)
print(s2)

# 중복 저장 불가
s2.add(4)
s2.add(5)
s2.add(5)

s1 = {1, 2, 3}
s2 = {2, 3, 4, 4}

# 합집합
print(s1.union(s2))
# 교집합
print(s1.intersection(s2))
# 차집합
print(s1.difference(s2))


mylist1 = [1, 2, 3, 4, 5]
# 다른 타입 자료도 저장 가능
mylist2 = [1, 2.0, "Hello"]

print(mylist1)

# 사람을 리스트로 정의
person = ['김철수', 20, 171.3, True]

print(person[0])
print(person[1])
print(person[-2])  # 뒤에서 두 번째
print(person[-1])  # 뒤에서 첫 번째

# 슬라이싱
# 0부터 (2-1)까지 범위 잘라내기
l = mylist1[0:2]
print(l)
l = mylist1[0:3]
print(l)

print(mylist1[3:])

print(mylist1[-3:-1])
print(mylist1[-4:])

print("Hello"[0:2])

r1 = list(range(0, 10))  # 범위는 0 ~ 9
r2 = list(range(1, 11))  # 범위는 1 ~ 10
print(r1)
print(r2)



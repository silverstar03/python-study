d1 = {}

# 키와 값 형식으로 데이터 저장
person = {}
person["name"] = "신수민"
person["age"] = 18
print(person)
print(person["name"])

d2 = {"a": "Hello", 1: 1000, (): [1, 2, 3], (1, 2): "3, 4"}
# 키는 보통 문자열 키 이용
# 키로 쓸 수 있는 타입은 불변 타입만 허용
print(d2["a"])
print(d2[1])
print(d2[()])
print(d2[(1,2)])

d3 = {'abc': 123, 'def': 456}
# KeyError: 0
# print(d3[0])
# print(d3[1])

d3['abc'] = 789


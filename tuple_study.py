# 튜플

t1 = 1, 1.23, "Hello"
t2 = (1, 1.23, "Hello")

print(type(t1))
print(t1)

# 불변(immutable) 자료형
# t1[0] = 2
print(t1[0])

person = ("김철수", 20, 171.3)
# 언팩킹
name, age, height = person
# a, b, c = [1, 2, 3]
# a, b, c = "abc"

# n, a = person
_, _, h = person
print(h)

t = (1)
print(type(t))
t = (1,)
print(type(t))


















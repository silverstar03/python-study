a = 100
b = 1.234
c = "Hello"
d = 'World'
e1 = "I'm here"
e2 = 'Tom said "Hello"'
e3 = 'I\'m here'

b1 = True # true
b2 = False # false

# 두 변수 동시 선언 및 값 초기화
# (엄밀히 말하자면 튜플을 언패킹하여 각각의 변수에 대입하는 것)
d, e = "d", 2

f = float(100)
i = int(10.234)
s = str(2345)

print(f)
print(i)
print(s)

f = 1234
# f = "Hello"
# f = [1, 2, 3, 4]

# print(str(f) + "haha")
#
# print(type(f))
# print(type(1.234))
# print(type("Hello"))
#
# print(isinstance(100, int))
# print(isinstance(1.234, float))
# print(isinstance("Hello", str))

# print(1, 2, 3)
# print(1, "b", 2.34)
# print("*", end="")
# print("*", end="")
# print("*", end="")
# print("*", end="")
# print("*")
# print("2020", "01", "01", sep="-")
# print("*" * 5)

# 주석

# 여러
# 줄
# 주석

"""
여러줄
주석
"""

'''
여러줄
주석
'''

s = "안녕" \
    "하세요."

ms = """안녕하세요.
반갑  습니다.
파이          썬
수업
입니다."""

print(ms)

# 안녕
# 하세요
# 여러줄
# 주석

a = [1, 2, 3]
b = a

print(id(a))
print(id(b))

# is와 ==의 차이
print(a is b)
print(a == b)

b = [1, 2, 3]
print(a is b)
print(a == b)


a = "World"
b = 1000
c = 1.234

# s = "Hello, %s, %d, %f" % (a, b, c)

# s = "Hello, {}, {}, {}".format(a, b, c)

# s = "Hello, {0}, {2}, {1}".format(a, b, c)

# f스트링

# s = f"Hello, {a}, {b}, {c}"

# s = "Hello, " + str(a) + "," + (str(b))


s = "Hello, +{},| {}, {}".format(a, b, c)
print(s)
# Hello, +World,| 1000, 1.234

s = f"{1 + 2} {'Hello'.upper()} {','.join(['a', 'b', 'c'])}"
print(s)
# 3 HELLO a,b,c

# 2진수, 16진수 표현
bi = 0b11111111
# 언더바(_) (4자리마다 끊으면 가독성 향상)
bi = 0b1111_1111  # 255
print(bi)
bi = 0b1111_1111_1111_1111  # 65535
print(bi)

h = 0xFF
# 마찬가지로 언더바 허용 (2자리마다 끊으면 가독성 향상)
h = 0xFF_FF
print(h)


# 과학적 표기법
a = 10e1
print(a)  # 100 (10 x 10^1)
a = 10e2
print(a)  # 1000 (10 x 10^2)
a = 10e-1
print(a)  # 1 (10 x 10^(-1)) => 10 x (1/10^1)
a = 10e-2
print(a)  # 0.1 (10 x 10^(-2)) => 10 x (1/10^2) => 10 x (1/100)





































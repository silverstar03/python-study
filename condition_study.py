if True:
    print("True")

if 1 == 1 and 2 > 1:
    print("True (1 == 1 and 2 > 1)")
    if True:
        print("True")

b = 5
if 1 < b and b <= 6:
    print("1 < 5 and 5 <= 6")

# 범위 비교 이런식으로 쓰는 것을 권장
if 1 < b <= 6:
    print("1 < 5 <= 6")

a = 1.1 + 2.2
print(a) # 3.3000000000000003

if a == 3.3:
    print("True") # 출력 X

if abs(a - 3.3) <= 0.00000001:
    print("True (abs(a - 3.3) <= 0.00001)")



import math

# 기본 rel_tol 값은 1e-9 (0.000000001)
if math.isclose(a, 3.3):
    print("True (math.isclose 함수 사용)")


if False:
    print("True")
else:
    print("False")

a = "Hello" if 1 == 1 else "World"
print(a)

b = (1 + 2 + 3) if (1 != 1) and (2 == 2) else "Hello".upper()
print(b)

score = 100
if score >= 90:
    print("Excellent")
elif score >= 80:
    print("Good")
elif score >= 70:
    print("Average")
else:
    print("Poor")

# False로 평가되는 Falsy 값
f = False
if f:
    print("True")

a = None
if a: print("True")
a = 0
if a: print("True")

a = ""
if a: print("True")
a = []
if a: print("True")
a = {}
if a: print("True")
a = ()
if a: print("True")




























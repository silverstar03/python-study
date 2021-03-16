# https://medium.com/@lazysoul/functional-programming-%EC%97%90%EC%84%9C-1%EA%B8%89-%EA%B0%9D%EC%B2%B4%EB%9E%80-ba1aeb048059

# 아래 3 가지조건을 충족한다면 1급 객체라고 할수 있습니다.
# 1. 변수나 데이타에 할당 할 수 있어야 한다.
# 2. 객체의 인자로 넘길 수 있어야 한다.
# 3. 객체의 리턴값으로 리턴 할수 있어야 한다.

def func():
    print("func")

a = func  # 1. 변수나 데이타에 할당 할 수 있어야 한다.

def func2(f):
    # 2. 객체의 인자로 넘길 수 있어야 한다.
    f()

    # 3. 객체의 리턴값으로 리턴 할수 있어야 한다.
    return f

print(type(a))  # <class 'function'>
b = func2(a)  # 1. 변수나 데이타에 할당 할 수 있어야 한다.
b()

# 결론 : 파이썬 언어에서 함수는 일급 객체(First-class citizen)다.

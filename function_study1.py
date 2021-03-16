# https://stackoverflow.com/questions/6434482/python-function-overloading
# https://stackoverflow.com/questions/8908760/should-i-use-camel-case-or-underscores-in-python

# def function_name(parameters):
# 	"""docstring"""
# 	statement(s)


def greet():
    print("Hello")

ret = greet()
print(ret)  # None 반환

# 반환값 있는 함수
def add(x, y):
    """add two parameters"""
    return x + y


print(add(2, 3))
print(add.__doc__)


# 튜플을 이용한 여러 값 반환 (실제로 반환되는 값은 하나, 튜플 객체)
# 물론 여러값 반환시 리스트 사용해서 반환해도 상관 없음
def arithmetics(x, y):
    return x + y, x - y, x * y, x / y

# Q) arithemtics_return_list 함수 만들어서 리스트로 반환하게 해보기


# 취향따라 dict 반환도 가능
def arithmetics2(x, y):
    return {
        "add": x + y,
        "sub": x - y,
        "mul": x * y,
        "div": x / y
    }

result = arithmetics(10, 5)
print(result)
print(type(result))
result = arithmetics2(10, 5)
print(result['add']); print(result['sub']); print(result['mul']); print(result['div'])


# 디폴트 값 부여
def say_greet_msg(name, msg="Hello"):
    print(msg, name)


say_greet_msg("김철수")
say_greet_msg("김철수", "안녕")
say_greet_msg(name="김철수")
say_greet_msg(name="김철수", msg="안녕")
# Python allows functions to be called using keyword arguments.
# When we call functions in this way, the order (position) of the arguments can be changed.
say_greet_msg(msg="안녕", name="김철수")
# 에러 (Positional argument after keyword argument)
# say_greet_msg(msg="안녕", "김철수")


# 디폴트 파라미터 주의점
"""
Default argument value is mutable
Inspection info: This inspection detects when a mutable value as list or dictionary is detected in a default value for an argument.
Default argument values are evaluated only once at function definition time, which means that modifying the default value of the argument will affect all subsequent calls of the function.
"""
# Default argument values are evaluated only once at function definition time
# 디폴트 값에는 불변 객체를 사용해야 함 (리스트는 변할 수 있는 (mutable) 객체)
# https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments

def make_list(*items, li=[]):
    for item in items:
        li.append(item)
    return li

print(make_list(1, 2, 3))
print(make_list(4, 5, 6))  # [1, 2, 3, 4, 5, 6]
# Q) 아래는 왜 잘 되는가?
print(make_list(4, 5, 6, li=[]))  # [4, 5, 6]

def make_list_fix(*items, li=None):
    if li is None:
        li = []
    for item in items:
        li.append(item)
    return li

print(make_list_fix(1, 2, 3))
print(make_list_fix(4, 5, 6))  # [4, 5, 6]

# 가변 인자 (Arbitrary Arguments)
def say_greet_msgs(*names, msg="Hello"):
    print(type(names)) # tuple
    for name in names:
        print(msg, name)

say_greet_msgs("김철수", "이영희", "신구", msg="헬로~")

# Q) my_sum 함수 정의 (가변 인자 숫자 받아서 다 더함)
def my_sum(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s

print(my_sum(1, 2, 3, 4))

# https://book.pythontips.com/en/latest/args_and_kwargs.html
def my_func(*args, **kwargs):
    print(type(kwargs)) # dict
    for a in args:
        print(a)

    for k, v in kwargs.items():
        print("key :", k, "value :", v)

my_func(1, 1.234, "Hello", a=1234, b="World")

# https://stackoverflow.com/questions/12555627/python-3-starred-expression-to-unpack-a-list
t = (1, 1.234, "Hello")
li = [1, 1.234, "Hello"]
li2 = ["Hello"]
d = {"a": 1234, "b": "World"}

my_func(*t, **d)
my_func(*li, **d)
# https://stackoverflow.com/questions/1952464/in-python-how-do-i-determine-if-an-object-is-iterable
"""
If the syntax *expression appears in the function call, expression must evaluate to an iterable. 
Elements from these iterables are treated as if they were additional positional arguments.
"""
"""
If the syntax **expression appears in the function call, expression must evaluate to a mapping, 
the contents of which are treated as additional keyword arguments.
"""
my_func(1, 1.234, *li2, **d, c="Bye")

# 주의 (기존에 정의된 함수(특히 빌트인 함수)를 덮어씌워 버리는 실수)
s = sum([1, 2, 3, 4])  # 10
print(sum)  # <built-in function sum>

# Shadows built-in name 'sum' 경고 발생
sum = 10
print(sum)  # 10

import builtins
import types

builtin_function_names = [name for name, obj in vars(builtins).items() if isinstance(obj, types.BuiltinFunctionType)]
print(builtin_function_names)
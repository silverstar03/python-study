# https://www.programiz.com/python-programming/anonymous-function
# https://stackoverflow.com/questions/25010167/e731-do-not-assign-a-lambda-expression-use-a-def
# https://towardsdatascience.com/python-lambda-function-b6e1fa3420c1
# https://treyhunner.com/2018/09/stop-writing-lambda-expressions/
double = lambda x: x * 2
add = lambda x, y: x + y

print(double(10))
print(add(2, 3))


# 람다를 반환하는 함수
def return_lambda_func(prefix=""):
    return lambda target: print(prefix, target)


f = return_lambda_func("안녕")
f("김철수")


def make_multiplier(mul=1):
    return lambda x: mul * x

mul1 = make_multiplier()
print(mul1(5))  # 5
mul2 = make_multiplier(10)
print(mul2(5))  # 50


# 람다는 한 줄 함수만 정의 가능하므로 두 줄 이상 써야 하면 일반 함수를 함수 내부에 정의하고 반환
# https://dojang.io/mod/page/view.php?id=2365
# https://dojang.io/mod/page/view.php?id=2366
# http://www.trytoprogram.com/python-programming/python-closures/
# https://www.includehelp.com/python/nonlocal-keyword-with-example.aspx
# https://stackoverflow.com/questions/1261875/python-nonlocal-statement
# https://stackoverflow.com/questions/4020419/why-arent-python-nested-functions-called-closures
# Firstly, a Nested Function is a function defined inside another function.
# It's very important to note that the nested functions can access the variables of the enclosing scope.
# However, at least in python, they are only readonly.
# However, one can use the "nonlocal" keyword explicitly with these variables in order to modify them.
def make_counter(init=0):
    start = init

    def counter():
        nonlocal start
        print(start)
        # 여기서 값을 변경하므로 nonlocal 키워드 필요
        start += 1

    return counter


c1 = make_counter()
c1(); c1(); c1()
c2 = make_counter(5)
c2(); c2(); c2()

# 람다 함수 사용처
# Python’s map and filter functions are used for looping over an iterable and making a new iterable
# that either slightly changes each element or filters the iterable down to only elements that
# match a certain condition. We can accomplish both of those tasks just as well with list comprehensions
# or generator expressions:
# https://book.pythontips.com/en/latest/map_filter.html
# Map applies a function to all the items in an input_list.
result = list(map(lambda x: x * 2, [1, 2, 3, 4]))
print(result)
# list comprehension으로도 map 기능 모방 가능
result = [x * 2 for x in [1, 2, 3, 4]]
print(result)

# As the name suggests, filter creates a list of elements for which a function returns true.
result = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
print(result)
# Q) list comprehension으로 filter 기능 모방해보기


from functools import reduce

# iterable의 첫 번째 요소가 시작 accumulator
s = reduce((lambda x, y: x + y), [1, 2, 3, 4])
p = reduce((lambda x, y: x * y), [1, 2, 3, 4])
r = reduce((lambda x, y: x + " " + y), ["Hello", "World", "Python"])
print(s)
print(p)
print(r)

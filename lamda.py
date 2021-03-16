# a = lambda : print("hello")
# a()

# r = list(filter(lambda name : len(name)==2, ["김구", "김철수", "김이영희", "박혁거세"]))
#
# print(r)

import random

# def make_list_generator(size, sum):
#     def result():
#         list = []
#         for i in range(size):
#             list.append(sum())
#         return list
#     return result

def make_list_generator(size, sum):
    list = []
    def result():
        for i in range(size):
            nonlocal list
            list.append(sum())
        return list
    return result


generator1 = make_list_generator(5, lambda: random.randint(1, 6))
print(generator1())

# 선생님 코드
# mlg = lambda size, f: lambda:[f() for i in range(size)]
# l = mlg (5, lambda : random.randint(1,6))
# print(l)
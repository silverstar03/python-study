print("a","b","c")
print("a"+"b"+"c")


print("{:f}".format(22.28))

print("{:.2f}".format(22.283))
print("{:.3f}".format(22.2237))

name="은별"
age=18
print(f"hello, {name}. You are {age}")


s="name: {}, number: {}, soccer: {}"
print(s.format("Ronaldo", 7, True))

print(type(age))


x="01::23::ab::&&"
y=x.split("::")
print(y)

h = "happy Programming"

print(h.replace("happy", "hi"))



print("{:d}".format(515))
print("{:+5d}".format(515))
print("{:-d}".format(515))
print("{:=-5d}".format(-515))

s = "{:+5d}, {:-05d}"
print(s.format(515,-515))


print("{:.2f}".format(12.335))

print("{:-12.2f}".format(-11.17))
print("{:=-12.2f}".format(-11.17))

print(f"이름 : {name}, 나이 : {age}".format("은별",18))

nums = list(range(3))

nums + [10, 11, 20]
nums.append([30,31])
print(nums)

a = list(range(1,10,2))
print(a)

print(set(range(1,10)))

print(range(1,10))


def sum(*args):
    add = 0
    for i in range(len(args)):
        add = add + args[i]
    return add

result1=sum(1, 2, 3, 4, 5)

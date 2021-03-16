class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + self.age


import pickle

p = Person("김철수", 20)
# other = Person("이영희", 30)

d = pickle.dumps(p)
print(d)
print(type(d))


# 역직렬화
# rbytes = open("tmp/person.bin", 'rb').read()
# unpickled_person = pickle.loads(rbytes)
# print(unpickled_person)


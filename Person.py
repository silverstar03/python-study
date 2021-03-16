class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def greet(self, target):
        print(self.name, ": 안녕 !", target)

    @classmethod
    def dec_count(cls):
        cls.count -= 1

    @classmethod
    def create_person(cls):
        return cls("무명씨", 1)

p1 = Person("강은별", 18)
p2 = Person("신수민", 18)
p1.greet("신수민")

print(Person.count)
Person.dec_count()
print(Person.count)
#1
#def cute_word(word):
#   num = "0123456789"
#   s = list(word)
#   for i in word:
#        if num in word:
#            word.replace(word[num], "삐")

#   return word


#print(cute_word("저기 152번 버스 온다."))



class BankAccount:
    def __init__(self, price):
        self.price = price

    def deposit(self, add_price):
        self.price += add_price

    def withdraw(self, out_price):
        if self.price < out_price:
            print("잔고가 부족합니다.")
        elif self.price > out_price:
            self.price -= out_price

    def __str__(self):
        return "balance : " + str(self.price)


ba = BankAccount(1000)
print(ba)
ba.deposit(2000)
print(ba)
ba.withdraw(5000)
print(ba)
ba.withdraw(1200)
print(ba)


# 3
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     def Point
#
#
# p1 = Point(2,3)
# p2 = Point(-2, -2)
#
# print(p1.x)
# print(p2.y)
#
# print(p1.distance(p2))
#
# print(p2.distance(p1))


# 4
class App:
    def __init__(self, app_name, category, price):
        self.app_name = app_name
        self.category = category
        self.price = price

    # @property
    def get_name(self):
        return self.app_name[:]

    # @get_name.setter
    def set_name(self, name):
        self.app_name = name

    # @property
    def get_category(self):
        return self.category[:]

    # @get_category.setter
    def set_category(self, category):
        self.category = category

kakaottok = App("카카오똑", "SNS", 0)
kartrice = App("카트라이스", "game", 1000)
facecook = App("페이스쿡", "SNS", 100)
apps = [kakaottok, kartrice, facecook]
for app in apps:
    if app.get_category() == "SNS":
        print(app.get_name())

# 5
class Todo:
    def __init__(self, do, rank):
        self.do = do
        self.rank = rank

    #@property
    def get_text(self):
        return self.do

    #get_text.setter
    def set_text(self, do):
        self.do = do

    #property
    def get_priority(self):
        return self.rank

    #@get_priority.setter
    def set_priority(self, rank):
        self.rank = rank

game = Todo('게임하기', 10)
sing = Todo("노래하기", 30)
dance = Todo('춤추기', 20)
todos = [game, sing, dance]
max_priority_todo = todos[0]

for todo in todos:
    if max_priority_todo.get_priority() < todo.get_priority():
        max_priority_todo = todo
print(str(max_priority_todo.get_text()))

class gugudan:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def gugu(self):
        for i in range(self.start, self.finish+1):
            for j in range(1, 10):
                print(i, 'X', j, '=', i*j)
            print("")


g1 = gugudan(3, 5)
g1.gugu()
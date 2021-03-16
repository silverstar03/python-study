class mirim:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def print(self):
        print(self.name + "은(는) " + self.major + "과 입니다.")

m = mirim("강은별","뉴미디어 소프트웨어")
m.print()


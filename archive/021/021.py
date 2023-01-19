class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("-1-")


class Fish:
    def swim(self):
        print("-2-")


# Inherit from both the Animal and Fish class
class Amphibian(Animal, Fish):
    def __init__(self):
        super().__init__()
        self.eyes = 3

    def swim(self):
        print("-3-different-")


nemo = Fish()
nemo.swim()

amber = Amphibian()
print(amber.eyes)
amber.breathe()
amber.swim()

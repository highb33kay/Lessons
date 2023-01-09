class Sum_Of_Numbers:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def summed(self, x, y):
        return x + y


first = Sum_Of_Numbers(1, 2)
print(first.summed(50, 36))
print(first.summed(100, 360))

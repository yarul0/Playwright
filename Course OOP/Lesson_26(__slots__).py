class Point:
    def __init__(self, x, y):
        self.x = x
        self.y =y


class Point_2nd:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

p2 = Point_2nd(2, 4)
p2.x = 30
# p2.z = 90
print(p2.x, p2.y)

# p1 = Point
# p1.__sizeof__() + p1.__dict__.__sizeof__()
# p2.__sizeof__()
class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D(Point2D):
    __slots__ = 'z',
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

p3 = Point3D(10, 20, 30)
print(p3.z)
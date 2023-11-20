class Integer:
    @classmethod
    def ver_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Should be INT value')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.ver_coord(value)
        setattr(instance, self.name, value)


class Point:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point(1, 2, 4)
print(p.__dict__, p.z)

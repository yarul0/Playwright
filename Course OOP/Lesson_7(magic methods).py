class Depo:
    MAX_Value = 100
    MIN_value = 1

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def set_values(self, x, y):
        if self.MIN_value <= x <= self.MAX_Value:
            self.__x = x
            self.__y = y

    @classmethod
    def set_bounds(cls, left, right):
        cls.MIN_value = left
        cls.MAX_Value = right

    def __getattribute__(self, item):
        if item in ('z', 'v'):
            raise AttributeError('PTN PNX')
        else:
            object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key in ('z', 'v'):
            raise AttributeError('PTN PNX')
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        print('wrong attr : ' + item)

    def __delattr__(self, item):
        print(f'--The next attr is deleted: {item}')
        object.__delattr__(self, item)




xc = Depo(111, 22)
xc.zv = 9
xc.kol = 77
xc.kolos = xc.pr
del xc.kolos

xc.set_bounds(0, 101)
print(xc.__dict__)





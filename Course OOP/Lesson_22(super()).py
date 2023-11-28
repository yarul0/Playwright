class Parent:
    name = 'Yaros'

    def __init__(self, x, y):
        print(f'init Parent for {self.__class__}')
        self._x = x
        self._y = y


class Sub_cl1(Parent):
    def draw(self):
        print('Output the First subclass')


class Sub_cl2(Parent):
    def __init__(self, x, y, new=None):
        super().__init__(x, y)
        self._new = new
        print('Output the Seconds subclass')

    def draw(self):
        print('Output the Second subclass')



s1 = Sub_cl1(1, 2)
s2 = Sub_cl2(4, 5)
class Parent:
    name = 'Yaros'

    def __init__(self, x, y):
        print(f'init Parent for {self.__class__}')
        self.__x = x
        self.__y = y


class Sub_cl2(Parent):
    def __init__(self, x, y, new=None):
        super().__init__(x, y)
        self.__new = new
        print('Output the Seconds subclass')

    def get_coords(self):
        return (self.__x, self.__y)


s2 = Sub_cl2(1, 5, 'none')
print(s2.get_coords())
print(s2.__dict__)
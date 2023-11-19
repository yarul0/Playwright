class Depo:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @classmethod
    def __check_values(cls, x):
        return type(x) in (int, float)

    def set_values(self, x, y):
        if self.__check_values(x) and self.__check_values(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Input should be integer')

    def get_values(self):
        return self.__x, self.__y


it = Depo(11, 23)
# print(Depo.x, Depo.y)
it.set_values(23, 44)
print(it.get_values())

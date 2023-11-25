class Bool:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __len__(self):
        return self.__x * self.__x + self.__y * self.__y

    def __bool__(self):
        return self.__x == self.__y

p = Bool(0, 0)
print(bool(p))
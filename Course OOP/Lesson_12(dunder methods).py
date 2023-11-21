class Train:
    def __init__(self, name):
        self.__name = name

    def __repr__(self):
        return f'{self.__class__}: {self.__name}'

    def __str__(self):
        return f'{self.__name}'


tr = Train('VL-11')
print(tr)
print(str(tr))
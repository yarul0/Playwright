class Derivate:
    def __init__(self, chart):
        self.__counter = 0
        self.__chart = chart

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('Input should be string')

        return args[0].strip(self.__chart)

d = Derivate
print(d)
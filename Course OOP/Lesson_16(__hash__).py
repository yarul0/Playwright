class Hash:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __eq__(self, other):
        return self.__x == other.x and self.__y == other.y

    def __hash__(self):
        return hash((self.__x, self.__y))


h1 = Hash(1, 2)
h2 = Hash(1, 2)
print(hash(h1), hash(h2), sep='\n')

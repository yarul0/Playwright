class Day:
    __Day = 86400

    def __init__(self, seconds: int):
        if type(seconds) != int:
            raise TypeError('Should be only INT')
        self.seconds = seconds % self.__Day

    @classmethod
    def ver_data(cls, other):
        if not isinstance(other, (int, Day)):
            raise  TypeError('Should be INT or Day')
        return other if isinstance(other, int) else other.seconds
    def __eq__(self, other):
        sc = self.ver_data(other)
        return self.seconds == sc
    def __lt__(self, other):
        sc = self.ver_data(other)
        return self.seconds < sc
    def __le__(self, other):
        sc = self.ver_data(other)
        return self.seconds <= sc





d1 = Day(1000)
d2 = Day(1001)
print(d1 < d2)

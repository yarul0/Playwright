class Day:
    __Day = 86400

    def __init__(self, seconds: int):
        if type(seconds) != int:
            raise TypeError('Should be only INT')
        self.seconds = seconds % self.__Day

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{self.get_formated(h)}:{self.get_formated(m)}:{self.get_formated(s)}'


    @classmethod
    def get_formated(cls, x):
        return str(x).rjust(2, '0')

    def __add__(self, other):
        if not isinstance(other, (int, Day)):
            raise ArithmeticError('Right amount should be INT')
        sec = other
        if isinstance(other, Day):
            sec = other.seconds
        return Day(self.seconds + sec)



day = Day(186399)
time = day + 21
time2 = Day(50000)
total = time + time2
print(day.get_time())
print(time.get_time())
print(time2.get_time())
print(total.get_time())
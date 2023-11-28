class FRange:
    def __init__(self, start=0.0, stop=0.0, step=0.0):
        self._start = start
        self._stop = stop
        self._step = step

    def __iter__(self):
        self._value = self._start - self._step
        return self
    def __next__(self):
        if self._value + self._step < self._stop:
            self._value += self._step
            return self._value
        else:
            raise  StopIteration

fr = FRange(0, 2, 0.5)

for x in fr:
    print(x)
# print(fr.__next__())
# print(fr.__next__())
# print(fr.__next__())
# print(next(fr))




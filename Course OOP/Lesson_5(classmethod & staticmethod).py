class Depo:
    zam = 0
    nach = 100

    @classmethod
    def validate(cls, arg):
        return cls.zam <= arg <= Depo.nach


    def __init__(self, inst, mash):
        self.inst = self.mash = 0
        if self.validate(inst) or self.validate(mash):
            self.inst = inst
            self.mash = mash

    def get_colona(self):
        return self.inst, self.mash

    @staticmethod
    def kvadrat(x, y):
        return x*y + y/x




col = Depo(230, 34)
print(Depo.validate(20))
status = col.get_colona()
print(status)
print(Depo.kvadrat(3, 9))



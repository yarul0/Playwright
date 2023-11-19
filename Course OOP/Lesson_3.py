class Yarul0:
    "Батьківський класс: вік, вага, стать"
    age = 39
    weight = 85
    gender = 'MALE'


    def __init__(self, x=11, y=22):
        print('виклик ініт' + str(self))
        self.x = x
        self.y = y
    def __del__(self):
        print('delete the class exmple: ' + str(self))
        print(pr.__dict__)


pr = Yarul0()
# print(pr.__dict__)
print(Yarul0.__dict__)



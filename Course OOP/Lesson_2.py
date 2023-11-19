class Yarul0:
    "Батьківський класс: вік, вага, стать"
    age = 39
    weight = 85
    gender = 'MALE'

    def print_param(self):
        print('print the method/function  ' + str(self))

    def set_param(self, x, y):
        self.x = x
        self.y = y

    def get_param(self):
        return (self.x, self.y)

# Yarul0.print_param()

pr = Yarul0()
# pr.set_param
# <bound method Yarul0.set_param of <__main__.Yarul0 object at 0x101dd9be0>>

pr_2 = Yarul0()

pr.set_param('one', 'two')
pr_dict = pr.__dict__
print(f'1st method - {pr_dict}')

pr_2.set_param('69', 69)
pr2_dict = pr_2.__dict__
print(f'2nd method - {pr2_dict}')
print()
print(f'1st method - {pr.get_param()}')
print(f'2nd method - {pr_2.get_param()}')
print()
print()
atr1 = getattr(pr, 'set_param')
atr2 = getattr(pr_2, 'set_param')
print(atr1)
print(atr2)
print()
print()
atr3 = getattr(pr, 'get_param')
atr4 = getattr(pr_2, 'get_param')
print(atr3())
print(atr4())





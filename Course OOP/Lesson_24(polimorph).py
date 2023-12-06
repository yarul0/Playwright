class Parent:
    def get_pr(self):
        raise NotImplementedError(f'Class {self.__class__} must have get_pr func')
class Box(Parent):
     def __init__(self, height, wight):
         self.height = height
         self.wight = wight

     # def get_param(self):
     #     return 2*(self.height + self.wight)
     #
     def get_pr(self):
         return 2*(self.height + self.wight)


class Cilinder(Parent):
    def __init__(self, radius):
        self.radius = radius

    # def get_cilinder(self):
    #     return (2 * 3.14 * self.radius)

    def get_pr(self):
        return (2 * 3.14 * self.radius)


b1 = Box(2,4)
b2 = Box(6, 5)

c1 = Cilinder(5)
c2 = Cilinder(9)

poli = [b1, b2, c1, c2]
for i in poli:
    print(i.get_pr().__round__(2))
# print(b1.get_param(), b2.get_param())
# print(c1.get_cilinder().__round__(2), c2.get_cilinder())
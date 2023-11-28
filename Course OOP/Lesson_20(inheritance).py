class Parent:
    name = 'Junior'

class Sub_class(Parent):
    def prin(self):
        print('Print parent class name')

p = Parent()
sub = Sub_class()
print(sub.name)

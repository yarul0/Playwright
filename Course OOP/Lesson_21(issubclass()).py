class Parent:
    pass

class Sub_Parent(Parent):
    pass

class Sub_class(list):

    def __str__(self):
        return ' '.join(map(str, self))


# p = Parent()
s = Sub_class([1, 2, 4])
print(issubclass(Sub_Parent, Parent))
print(s)

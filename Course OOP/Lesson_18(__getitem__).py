class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        return self.marks[item]

    def __setitem__(self, key, value):
        if key > len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)
        self.marks[key] = value

    def __delitem__(self, key):
        del self.marks[key]

s1 = Student('Yaros', [5, 4, 2, 3, 1])
s1[10] = 90
del s1[4]

print(list(s1))
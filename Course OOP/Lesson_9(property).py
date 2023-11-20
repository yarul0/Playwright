class Persona:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age


person = Persona("John", 25)
del person.age
print(person.__dict__)  # Accessing the updated age attribute
person.age = 69
print(person.__dict__)

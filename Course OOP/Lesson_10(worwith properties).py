from string import ascii_letters
class Persona:
    S_UA = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ-"
    S_UA_UPPER = S_UA.lower()


    def __init__(self, fio, age, passport, weight):
        self.ver_fio(fio)

        self.__fio = fio
        self.__age = age
        self.__passport = passport
        self.__weight = weight

    @classmethod
    def ver_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('FIO should be a string value')

        f = fio.split()
        if len(f) != 3:
            raise TypeError('Incorrect data format')

        letters = ascii_letters + cls.S_UA + cls.S_UA_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError('FIO should be at least one letter')
            elif len(s.strip(letters)) != 0:
                raise TypeError('Should be only Ukrainian letters and "-"')

    @classmethod
    def ver_age(cls, age):
        if type(age) != int or 14 > age or age > 120:
            raise TypeError('Incorrect data format')

    @classmethod
    def ver_weight(cls, weight):
        if type(weight) != float or 20 > weight:
            raise TypeError('Incorrect data format')

    @classmethod
    def ver_passport(cls, passport):
        if type(passport) != int or passport > 999999999:
            raise TypeError('Passport should be a string value')

    @property
    def fio(self):
        return self.__fio

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.ver_age(age)
        self.__age = age

    @property
    def passport(self):
        return self.__passport
    @passport.setter
    def passport(self, passport):
        self.ver_passport(passport)
        self.__passport = passport

    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, weight):
        self.ver_weight(weight)
        self.__weight = weight




person = Persona('Передерій Ярослав Мик-ч', 38, '1234 567890', 85.2)
person.age = 43
person.passport = 123456789
person.weight = 80.9
print(person.__dict__)
print(person.age)

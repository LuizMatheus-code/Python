#usr/local/bin/python3
from abc import ABCMeta, abstractproperty

class Human(metaclass=ABCMeta):
    # class attribute below
    species = 'Homo Sapiens'

    def __init__(self, name):
        self.name = name
        self._age = None


    @abstractproperty
    def inteligence(self):
        pass


    
    @property
    def age(self):
        return self._age

    
    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError('the age has to be a positive number')
        self._age = age


    def ancient(self):
        self.species = 'Homo Neanderthalensis'
        return self


    @staticmethod
    def species_example():
        adjectives = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return('Australopithecus', ) + tuple(f'Homo {adj} ' for adj in adjectives)

    @classmethod
    def is_evolution(cls):
        return cls.species == cls.species_example()[-1]


class Neanderthal(Human):
    species = Human.species_example()[-2]


    @property
    def inteligence(self):
        return False


class HomoSapiens(Human):
    species = Human.species_example()[-1]


    @property
    def inteligence(self):
        return True


class Animal:
    @property
    def abilities(self):
        return ('sleep', 'eat', 'drink')


class Human_being(Animal):
    @property
    def abilities(self):
        return super().abilities + ('think', 'speak', 'study')


class Spider(Animal):
    @property
    def abilities(self):
        return super().abilities + ('climb', 'bite')


class SpiderMan(Human_being, Spider):
    @property
    def abilities(self):
        return super().abilities + \
            ('reflexes', 'super strength')

class CrystalGems:
    def __str__(self):
        formating = super().__str__().replace('(', '{[').replace(')', ']}')
        return f"<>{formating}<>"


class Person:
    def __init__(self, name):
        self.name = name

    
    def __str__(self):
        return self.name

    
class Creature:
    def __init__(self, name, animal=True):
        self.name = name
        self.animal = animal
    
    def __str__(self):
        return self.name + ' (animal)' if self.animal else ''


class CrystalPerson(CrystalGems, Person):
    pass


class CrystalCreature(CrystalGems, Creature):
    pass


class RGB:
    def __init__(self):
        self.colors = ['red', 'green', 'blue'][::-1]


    def __iter__(self):
        return self


    def __next__(self):
        try:
            return self.colors.pop()
        except IndexError:
            raise StopIteration()


class SimpleClass:
    pass


if __name__ == '__main__':
    lis = [SimpleClass, SimpleClass, SimpleClass]
    print(lis.count(SimpleClass))

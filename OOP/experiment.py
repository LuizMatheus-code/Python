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


if __name__ == '__main__':
    """try:
        jose = Human('Jhon')
        print(jose.inteligence)
    except TypeError as error:
        print(error)"""

    k = Neanderthal('kable')
    print('{} of the class {}, inteligence {}'
        .format(k.name, k.__class__.__name__, k.inteligence))
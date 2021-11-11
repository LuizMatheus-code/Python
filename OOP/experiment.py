#usr/local/bin/python3
class Human:
    # class attribute below
    species = 'Homo Sapiens'

    def __init__(self, name):
        self.name = name
        self._age = None


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


class HomoSapiens(Human):
    species = Human.species_example()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('Jose')
    gork = Neanderthal('gork')
    print(f'(class) Evolution {", ".join(HomoSapiens.species_example())}')
    print()
    print(f'(instance) Evolution {", ".join(jose.species_example())}')
    print(f'is it evolution? {HomoSapiens.is_evolution()}')
    print(f'is it evolution? {Neanderthal.is_evolution()}')

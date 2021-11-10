#usr/local/bin/python3
class Human:
    # class attribute below
    species = 'Homo Sapiens'

    def __init__(self, name):
        self.name = name


    def ancient(self):
        self.species = 'Homo Neanderthalensis'
        return self


    @staticmethod
    def species_example():
        adjectives = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return('Australopithecus', ) + tuple(f'Homo {adj} ' for adj in adjectives)


if __name__ == '__main__':
    jose = Human('Jose')
    Human.ancient(jose)
    Gork = Human('Gork').ancient()
    
    print(Human.species)
    print(jose.species)
    print(Gork.species)

from datetime import datetime

class Person:
    current_year = datetime.now().year
    weapon = "sword"

    def __init__(self, name, age, fighting=False, sleeping=False):
        self.name = name
        self.age = age
        self.fighting = fighting
        self.sleeping = sleeping


    def fight(self, enemy):
        if self.sleeping:
            print(f"{self.name} can't fight while sleeping")
        else:
            self.fighting = True
            print(f'{self.name} is fighting against {enemy}')
            return 

    @classmethod
    def weaponry(cls, name):
        print(f'{name} uses a {cls.weapon} as a weapon')


    @staticmethod
    def call_jake(name, jake_name='Jake, the dog'):
        print(f'{name} is calling {jake_name}')

    def sleep(self):
        self.sleeping = True
        print(f'{self.name} is sleeping. Z...Z...Z')


    def year_of_being_born(self):
        final_year = self.current_year - self.age
        print(f'{self.name} was born in {final_year}')


    @classmethod
    def by_year_of_being_born(cls, name, year):
        return cls(name, year)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    
    def reduce_price(self, percentage=0):
        self.price -= (self.price * (percentage/100))
        return self.price


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, value):
        self._name = value.title()


    #getter
    @property
    def price(self):
        return self._price
    

    #setter
    @price.setter
    def price(self, value):
        if isinstance(value, str):
            value = float(value.replace("R$", ''))
        self._price = value
    

class DataBase:
    '''a class representing a data base'''
    def __init__(self):
        self.__data = {}

    def insert_client(self, id, name):
        if 'clients' not in self.__data:
            self.__data['clients'] = {id: name}
        else:
            self.__data['clients'].update({id: name})
    
    
    def client_list(self):
        for id, name in self.__data['clients'].items():
            print(id, name)


    def erase_client(self, id):
        del self.__data['clients'][id]
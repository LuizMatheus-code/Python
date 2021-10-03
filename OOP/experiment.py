from datetime import datetime
from random import randint

class Person():
    current_year = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, name, age, speaking=False, eating=False):
        self.name = name
        self.age = age
        self.speaking = speaking
        self.eating = eating


    def eat(self):
        if self.eating:
            print(f'{self.name} is already eating')
            return
        elif self.speaking:
            print(f'{self.name} cannot eat while speaking')
            return
        else:
            print(f'{self.name} started eating')
            self.eating = True
            return self.eating


    def stop_eating(self):
        if not self.eating:
            print(f'{self.name} is not eating')
        else:
            self.eating = False
            print(f'{self.name} stopped eating')
            return self.eating
    

    def speak(self, subject):
        if self.eating:
            print(f'{self.name} needs to stop eating first')
        elif self.speaking:
            print(f'{self.name} is already speaking')
        else:
            print(f'{self.name} is talking about {subject}')
            self.speaking = True
            return self.speaking


    def get_year(self):
        return self.current_year - self.age

    @classmethod
    def use_year(cls, name, year_born):
        age = cls.current_year - year_born
        return cls(name, age)
    
    @staticmethod
    def ID_generator():
        rand = randint(10000, 19999)
        return rand

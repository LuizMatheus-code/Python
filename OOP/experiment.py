from datetime import datetime

class Person:
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

    def sleep(self):
        self.sleeping = True
        print(f'{self.name} is sleeping. Z...Z...Z')


    def year_of_being_born(self):
        current_year = datetime.now().year
        final_year = current_year - self.age
        print(f'{self.name} was born in {final_year}')


from datetime import datetime

class Product:
    def __init__(self, salesman, data, value):
        self.salesman = salesman
        self.data = data
        self.value = value


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

    def __str__(self):
        #converts the object to a string with name and age
        return f'{self.name} is {self.age} year(s) old'


    def is_adult(self, verification=None):
        '''it verifies if the object has more than 18 years.'''
        if self.age >= 18:
            verification = True
        else:
            verification = False
        return verification


class Salesman(Person):
    def __init__(self, name, age, salary):
        self.age = age
        self.name = name
        self.salary = salary
    

    def __str__(self):
        self.salary = float(self.salary)
        return f'{self.name} is {self.age}, gaining {self.salary} as a salary'


class Client(Person):
    def __init__(self, name, age):
        self.age = age
        self.name = name
        self.grocery_list = []


    def register_groceries(self, Product):
        self.grocery_list.append(Product)
        return self.grocery_list
    
    def get_last_product(self):
        return self.grocery_list[-1]


    def total_groceries(self):
        total = 0
        for thing in self.grocery_list:
            total += thing.value
        return total


cat = Client('gumball', 12)
rock = Salesman('Larry Needlemeyer', 20, 2000)
glasses = Product(rock, datetime.now(), 100)
helmet = Product(rock, datetime.now(), 200)
cat.register_groceries(glasses)
cat.register_groceries(helmet)
print(f'Client: {cat}', '(adult)' if cat.is_adult() else '')
print(f'Salesman: {rock}')
print(f'''Total of {len(cat.grocery_list)} products ($ {cat.total_groceries()})
Last product: {cat.get_last_product().data}''')

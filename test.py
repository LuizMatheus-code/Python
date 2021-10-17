from datetime import datetime


class Project:
    def __init__(self, name):
        self.name = name
        self.task_list = []
    

    def add(self, description):
        self.task_list.append(Task(description))


    def due(self):
        return [element for element in self.task_list if not element.done]


    def search(self, description):
        #IndexError
        return [element for element in self.task_list if element.description == description][0]
    

    def __str__(self):
        return f'{self.name} | {len(self.due())} task(s) due |'


class Task:
    def __init__(self, description):
        self.description = description
        self.done = False
        self.creation = datetime.now()


    def getting_done(self):
        self.done = True
    

    def __str__(self):
        return self.description + (' (Done)' if self.done else '')


def main():
    house = Project('House tasks')
    house.add('Laundry')
    house.add('Dishes')
    print(house)

    house.search('Dishes').getting_done()
    for tar in house.task_list:
        print(f'- {tar}')
    print(house, '\n')

    merchandise = Project('To buy')
    for x in range(1, 4):
        merchandise.add(f'thing {x}')
    print(merchandise)

    thing_1_search = merchandise.search('thing 1')
    thing_1_search.getting_done()
    for y in merchandise.task_list:
        print(f'- {y}')
    print(merchandise)

if __name__ == '__main__':
    main()

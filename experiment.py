from datetime import datetime

class Project:
    def __init__(self, name):
        self.name = name
        self.task = []


    def add(self, description):
        self.Task.append(Task(description))


    def missing(self):
        return [Task for Task in self.Task if not Task.conclusion]
    

    def search(self, description):
        return [Task for Task in self.task
        if Task.description == description][0]

    def __str__(self):
        return f'{self.name} ({len(self.missing())}) missing tasks'

class Task:
    def __init__(self, description):
        self.description = description
        self.done = False
        self.creation = datetime.now()


    def conclusion(self):
        self.done = True


    def __str__(self):
        return self.description + (' concluded' if self.done else '')


def main():
    house = Project('house')
    house.add('dishes')
    house.add('clean the house')
    print(house)

    house.search('dishes')


if __name__ == '__main__':
    main()

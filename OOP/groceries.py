from datetime import datetime, timedelta


class TaskNotFound(Exception):
    pass


class Project:
    def __init__(self, name):
        self.name = name
        self.task_list = []


    def __iter__(self):
        return self.task_list.__iter__()

    

    def __iadd__(self, task):
        task.owner = self
        self.add_task(task)
        return self


    def add_task(self, task, **kwargs):
        self.task_list.append(task)


    def add_new_task(self, description, **kwargs):
        self.task_list.append(Task(description, kwargs.get('end', None)))


    def add(self, task, end=None, **kwargs):
        function = self.add_task if isinstance(task, Task) \
            else self.add_new_task
        kwargs['end'] = end
        function(task, **kwargs)


    def due(self):
        return [element for element in self.task_list if not element.done]


    def search(self, description):
        try:
            return [element for element in self.task_list if element.description == description][0]
        except IndexError as error:
            raise TaskNotFound(str(error))
    

    def __str__(self):
        return f'{self.name} | {len(self.due())} task(s) due |'


class Task:
    def __init__(self, description, end=None):
        self.description = description
        self.done = False
        self.creation = datetime.now()
        self.end = end


    def getting_done(self):
        self.done = True
    

    def __str__(self):
        status = []
        if self.done:
            status.append('(Done)')
        elif self.end:
            if datetime.now() > self.end:
                status.append('(Late)')
            else:
                count_days = (self.end - datetime.now()).days
                status.append(f"You're late by {count_days} days")
        return f'{self.description}' + ' '.join(status)
    

    def test():
        pass


    def test(a, b, c):
        pass


class RecurrentTask(Task):
    def __init__(self, description, end, days=7):
        super().__init__(description, end)
        self.days = days
        self.owner = None

    def getting_done(self):
        super().getting_done()
        new_end = datetime.now() + timedelta(days=self.days)
        new_task = RecurrentTask(self.description, new_end, self.days)
        if self.owner:
            self.owner += new_task
        return new_task


def main():
    house = Project('House tasks')
    house.add('Laundry')
    house.add('Dishes')
    house += RecurrentTask('clean the house', datetime.now(), 7)
    house.search('clean the house').getting_done()
    print(house)

    try:
        house.search('Dishes - error').getting_done()
    except TaskNotFound as error:
        print(f'the cause was {str(error)}!')

    house.search('Dishes').getting_done()
    for tar in house:
        print(f'- {tar}')
    print(house, '\n')

    merchandise = Project('To buy')
    for x in range(1, 4):
        merchandise.add(f'thing {x}')
    print(merchandise)

    thing_1_search = merchandise.search('thing 1')
    thing_1_search.getting_done()
    for y in merchandise:
        print(f'- {y}')
    print(merchandise)

if __name__ == '__main__':
    main()

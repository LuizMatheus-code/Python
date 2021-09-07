from datetime import datetime

person_data = dict()
name = input('name: ')
year_born = int(input('type the year the person was born: '))
work_card = int(input("type the work card [0 = don't have one]: "))
current_year = datetime.now().year
age = current_year - year_born
person_data['name'] = name
person_data["age"] = age
if work_card == 0:
    if age < 18:
        time_left = 18 - age
        print(f"in {time_left} years in the future, the person will work")
    else:
        print('the person can already work')
else:
    year_of_work = int(input('type the year you started to work: '))
    salary = float(input('type the salary: '))
    person_data['year of work'] = year_of_work
    person_data['salary'] = salary
    if age < 65:
        retirement = 65 - age
        person_data['retirement'] = retirement

for key, items in person_data.items():
    print(f'the {key} is: {items}')

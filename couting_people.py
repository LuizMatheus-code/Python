people_name = []
median_age = 0
total_people = 0
print('type 0 (zero) at any time to stop.')
while True:
    name = str(input('type the name: ')).strip()
    if name == '0':
        break
    people_name.append(name)
    age = int(input('type the age: '))
    if age == 0:
        break
    else:
        median_age += age
    print('[1] Male\n[2] Female\n[3] Other')
    gender = ''
    while gender != 0:
        gender = int(input('type here: '))
        if gender != 1 and gender != 2 and gender != 3:
            print('type one of the alternatives')
        else:
            break
    total_people += 1
median_age = median_age / total_people
print("""total of people: {};
median age of the people registered: {};""".format(total_people, median_age))
print("people's names: ", end='')
for person_registered in people_name:
    print(person_registered, end=' ')

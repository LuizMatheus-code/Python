#creating the dictionaries and lists that'll store the information
people_information = dict()
total_of_people = list()
women_registered = list()
#this serves to convert 1 and 2 to 'man' and 'woman'
gender_string = ["man", "woman"]
while True:
    name = input('type the name: ').strip()
    print('[1] Men\n[2] Women')
    #this part loops the user so that they have to choose between 1 or 2
    while True:
        gender = input('type the gender: ').strip()
        if gender == '1' or gender == '2':
            gender = int(gender)
            # this part converts 1 and 2 to men and women as explained before
            gender = gender_string[gender - 1]
            if gender == 'woman':
                women_registered.append(name)
            break
        else:
            print("Invalid.Type just 1 or 2")
    #this also loops the user to make them type a valid number
    while True:
        age = input('type the age: ').strip()
        if age.isdigit():
            age = int(age)
            if age <= 0:
                print('Invalid.Type a number that is bigger than zero')
            else:
                break
        else:
            print('Invalid.Type only numbers')
    #if things get this far, all the information is correct and it's time to add to the list
    people_information['name'] = name
    people_information['gender'] = gender
    people_information['age'] = age
    #this makes a copy of the dictionary so that the information doesn't overlap itself
    total_of_people.append(people_information.copy())
    print('[0] Stop\n[1] Continue')
    #this part asks if the user wants to continue and verifies if the answer is valid
    while True:
        continue_option = input('Do you wish to stop or continue? ').strip()
        if continue_option.isdigit():
            continue_option = int(continue_option)
            if continue_option == 0 or continue_option == 1:
                break
        else:
            print('invalid.Type only numbers')
    if continue_option == 0:
        break
print('=-' * 20)
#the average age receives the sum of all ages divided by the total of people
average_age = 0
for age_counter in range(0, len(total_of_people)):
    average_age += total_of_people[age_counter]['age']
average_age /= len(total_of_people)
# this part shows: the amount of people registered, the average age and the women registered
print(f'''total of people registered: {len(total_of_people)};
average age: {average_age};
women registered: ''', end='')
for elements in women_registered:
    print(elements, end=' ')
# this part just appears if there are no women registered
if len(women_registered) == 0:
    print("no women registered")
# it shows the: name, gender and age of people above age average
print("\npeople above the average age", end='')
for number in range(0, len(total_of_people)):
    if total_of_people[number]['age'] > average_age:
        for key, value in total_of_people[number].items():
            print(f'\n{key}: {value}', end="")
#this print is just to create another line and add aesthetic symbols
print()
print('=-' * 20)

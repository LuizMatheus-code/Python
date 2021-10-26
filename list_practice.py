

def calculate_weight():
    total_people = []
    heaviest_people = []
    lightest_people = []
    counting_people = 1
    while True:
        print(f"person {counting_people}")
        name = input('type the name: ').strip()
        weight = float(input('type the weight: '))
        total_people.append([name, weight])
        print("[0]Continue\n[1]Stop")
        confirmation = 2
        while confirmation != 1 and confirmation != 0:
            confirmation = int(input('type: '))
            if confirmation == 0:
                counting_people += 1
            elif confirmation == 1:
                break
            else:
                print("type only 0 or 1")
        if confirmation == 1:
            break
    biggest = total_people[0][1]
    lowest = total_people[0][1]
    for counter in range(1, len(total_people)):
        people_weight = total_people[counter][1]
        if people_weight > biggest:
            biggest = people_weight
        elif people_weight < lowest:
            lowest = people_weight
    for count in range (0, len(total_people)):
        analyse_weight = total_people[count][1]
        if analyse_weight == biggest:
            heaviest_people.append(total_people[count][0])
    for counting in range(0, len(total_people)):
        less_weight = total_people[counting][1]
        if less_weight == lowest:
            lightest_people.append(total_people[counting][0])
    print(f'''you registered {len(total_people)} people at total''')
    print(f'''heaviest {biggest}: {heaviest_people.sort()}''')
    print(f'''lightest {lowest}: {lightest_people.sort()}''')


def new():
    test = [i for i in range(100)]
    six = [x for x in test if '6' in str(x)]
    print(test)
    print(six)
    space_count = [letter for letter in 'Find all of the numbers from 1–1000 that have a 6 in them' if letter.isspace]
    print(len(space_count))
    remove_vowels = ''.join([item for item in 'Count the number of spaces in a string (use string above)' if item.lower() not in 'aeiou'])
    print(remove_vowels)


new()

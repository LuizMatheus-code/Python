

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
    generator = (i ** 2 for i in range(10) if i % 2 == 0)
    print(next(generator))
    print(next(generator))

    dic = {f'number {i}': i * 2 for i in range(5) if i % 2 == 0}
    for name, num in dic.items():
        print(f'{name}: {num}')


new()

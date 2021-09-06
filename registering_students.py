informations = []
counting_people = 0
while True:
    name = input("Type the name: ").strip()
    grade1 = float(input('Type the grade 1 (from 0 to 10): '))
    grade2 = float(input('Type the grade 2 (from 0 to 10): '))
    counting_people += 1
    grade_average = (grade1 + grade2) / 2
    informations.append([name, [grade1, grade2], grade_average])
    print('[0]Stop\n[1]Continue')
    continue_option = int(input('Type here: '))
    if continue_option == 0:
        break
print(f"""Number | Name | Grade average""")
for number, data in enumerate(informations):
    print(f'{number + 1:<7} {data[0]:<15} {data[2]:<8.1f}')
print('type the number of a student to see their grades. If you type "-1" the program stops')
while True:
    student_number = int(input('Type here: '))
    if student_number == -1:
        break
    if student_number <= len(informations):
        student_number -= 1
        print(f"{informations[student_number][0]}'s grades are {informations[student_number][1][0]} and {informations[student_number][1][1]}")
    else:
        print('Invalid. Type one of the numbers of the students')

first_number = float(input('type the first number: '))
second_number = float(input('type the second number: '))
print("""[1] Sum
[2] Subtraction
[3] Multiplication
[4] Division
[5] The bigger number
[6] Type again
[7] Exit""")
answer_options = [1, 2, 3, 4, 5, 6, 7]
while True:
    answer = input("type here: ")
    if answer.isnumeric():
        answer = int(answer)
        if answer in answer_options:
            if answer == 1:
                total_sum = first_number + second_number
                print('{} + {} = {}'.format(first_number, second_number, total_sum))
            elif answer == 2:
                Subtraction = first_number - second_number
                print('{} - {} = {}'.format(first_number, second_number, Subtraction))
            elif answer == 3:
                Multiplication = first_number * second_number
                print('{} x {} = {}'.format(first_number, second_number, Multiplication))
            elif answer == 4:
                Division = first_number / second_number
                print('{} / {} = {}'.format(first_number, second_number, Division))
            elif answer == 5:
                if second_number > first_number:
                    print('{} is bigger than {}'.format(second_number, first_number))
                elif second_number < first_number:
                    print('{} is bigger than {}'.format(first_number, second_number))
                else:
                    print('both {} and {} are the same'.format(first_number, second_number))
            elif answer == 6:
                print("type the new numbers")
                first_number = float(input('first new number: '))
                second_number = float(input('second new number: '))
                print("""[1] Sum\n[2] Subtraction\n[3] Multiplication\n[4] Division\n[5] The bigger number\n[6] Type again\n[7] Exit""")
            elif answer == 7:
                print("Successfully exited")
                break
        else:
            print('type only a number within the alternatives')
    else:
        print('type only numbers')

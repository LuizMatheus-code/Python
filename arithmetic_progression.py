showing_number = 0
current_term = 1
first_term = float(input('type the first term of the progression: '))
radio = float(input('type the radio: '))
term_number = int(input('type the number of the term you want to see: '))
print(first_term, end=" ")
showing_number = first_term
while True:
    showing_number += radio
    print(showing_number, end=" ")
    current_term += 1
    if current_term == term_number:
        print('\nDo you wish to continue?\n[1] Yes\n[2] No')
        exit_option = int(input("type here: "))
        if exit_option == 2:
            print('successfully exited')
            break
        else:
            first_term = float(input('\ntype the first term of the progression: '))
            radio = float(input('type the radio: '))
            term_number = int(input('type the number of the term you want to see: '))
            showing_number = 0
            current_term = 1
            print(first_term, end=" ")

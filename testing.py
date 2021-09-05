from random import randint

list_of_numbers = []
for x in range(0, 9):
    number = randint(1, 10)
    list_of_numbers.append([number])

count = 0
for elements in list_of_numbers:
    print(elements, end=" ")
    count += 1
    if count % 3 == 0:
        print()

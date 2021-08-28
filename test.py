# -*- coding: utf-8 -*-

group = list()
biggest = 0
lowest = 0
feedback = float(input("give me any number: "))
biggest = feedback
lowest = feedback
for counter in range(0, 2):
    group.append(feedback)
    feedback = float(input("give me any number: "))
    if feedback > biggest:
        biggest = feedback
    elif feedback < lowest:
        lowest = feedback
group.append(feedback)
print("""biggest {}
lowest {}
numbers given: """.format(biggest, lowest), end="")
for numbers in group:
    print(numbers, end=" ")

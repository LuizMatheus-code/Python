# -*- coding: utf-8 -*-

#collecting the information needed
first_number = float(input("type here the first measure of the triangle: "))
second_number = float(input("type here the second measure of the triangle: "))
third_number = float(input("type here the third measure of the triangle: "))

#verification of the measurements to find out if the triangle exists or not
first_condition = (second_number - third_number) < first_number < (second_number + third_number)
second_condition = (first_number - third_number) < second_number < (first_number + third_number)
third_condition = (first_number - second_number) < third_number < (first_number + second_number)

if first_condition and second_condition and third_condition: #it finds out in which classification the triangle is
    if first_number == second_number and second_number == third_number:
        print("""1: {}\n2: {}\n3: {}\nthe triangle is equilateral""".format(first_number, second_number, third_number))
    elif first_number != second_number and second_number != third_number and first_number != third_number:
        print("""1: {}\n2: {}\n3: {}\nthe triangle is scalene""".format(first_number, second_number, third_number))
    else:
        print("""1: {}\n2: {}\n3: {}\nthe triangle is isoceles""".format(first_number, second_number, third_number))
else: #this part only appears if the triangle does not exist
    print("""1: {}
2: {}
3: {}
the triangle doesn't exist""".format(first_number, second_number, third_number))

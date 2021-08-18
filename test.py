# -*- coding: utf-8 -*-

def Fibo(limit):
    before_last = 0
    last = 1
    print(before_last, last)
    while True:
        if last >= limit:
            break
        else:
            next_number = before_last + last
            print(next_number)
            before_last = last
            last = next_number


def Sequence(number):
    number = float(number)
    for first in range(1, 11):
        result = number * first
        print("{} x {} = {}".format(number, first, result))


def Hypotenuse(oposite_cathetus, adjacent_cathetus):
    oposite_cathetus = float(oposite_cathetus)
    adjacent_cathetus = float(adjacent_cathetus)
    hipo = (oposite_cathetus**2 + adjacent_cathetus**2)**(1/2)
    return hipo


import random

options = []
for num in range(1, 5):
    x = input('person {}: '.format(num))
    options.append(x)

choosen_one = random.choice(options)
print("choosen one: {} out of ".format(choosen_one), end="")

options.remove(choosen_one)
for elements in options:
    print(elements, end=" ")

# -*- coding: utf-8 -*-

number = int(input("insert number: "))
unity = number // 1 % 10
ten = number // 10 % 10
hundred = number // 100 % 10
thousand = number // 1000 % 10
print("unity: {}\nten: {}\nhundred: {}\nthousand: {}".format(
    unity,
    ten,
    hundred,
    thousand
))

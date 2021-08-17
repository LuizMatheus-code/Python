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

Fibo(100)

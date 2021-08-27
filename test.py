# -*- coding: utf-8 -*-

name = input("type here any name: ").strip()

# prints each letter of the first name until it's fully printed
print("first name: ", end='')
for first_lyrics in range(0, name.find(' ')):
    print(name[first_lyrics], end="")

#separates the two names and, then writes the last name
print("\nlast name: ", end="")
for last_lyrics in range(name.rfind(' ') + 1, len(name)):
    print(name[last_lyrics], end="")

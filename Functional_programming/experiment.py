list_1 = [1, 2, 3]
double = map(lambda x: x * 2, list_1)

print(list(double))

list_2 = [
    {'name': 'a', 'age': 1},
    {'name': 'b', 'age': 2},
    {'name': 'c', 'age': 3}
]

just_names = map(lambda p: p['name'], list_2)
print(list(just_names))

just_age = tuple(map(lambda p: p['age'], list_2))
print(list(just_age))
print(sum(just_age))

name_age = list(map(lambda data: (data['name'], data['age']), list_2))
for na, ag in name_age:
    print(na, ag)

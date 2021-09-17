values = ("gustavo", 1, 2)
x = "name {} age {} and {}".format(*values)
print(x)
folder = open("experiment.csv")
y = folder.read()
print(y)
folder.close()
for registering in y.splitlines():
    print('name {} and age {}'.format(*registering.split(', ')))

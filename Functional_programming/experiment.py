def mapping(func, lis):
    return (func(element) for element in lis)


xy = mapping(lambda x: x ** 2, [2, 3, 4])
print(list(xy))

def area(base, height):
    area = base * height
    return area


def decoration(word):
    word = str(word)
    length_word = len(word) + 2
    print('=' * length_word)
    print(word.center(length_word))
    print('=' * length_word)


def counting():
    start = int(input('start: '))
    end = int(input('end: '))
    steps = int(input('steps:'))
    for showing in range(start, end + 1, steps):
        print(showing, end=' ')


print(area(base=2, height=5))
decoration('coding')
counting()

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


def biggest(*numbers):
    amount_numbers = []
    for elements in numbers:
        amount_numbers.append(elements)
    bigger = amount_numbers[0]
    for checking in amount_numbers:
        if bigger < checking:
            bigger = checking
    return bigger


def factorial(*num):
    total_numbers = []
    final_result = []
    for elements in num:
        total_numbers.append(elements)
    for number_used in total_numbers:
        final_factorial = 1
        for count in range(number_used, 0, -1):
            final_factorial *= count
        final_result.append(final_factorial)
    return final_result


print(area(base=2, height=5))
decoration('coding')
print(biggest(10, 2,3 , 5, 6, 11))
x = factorial(5, 3, 2, 4, 6)
print(x)

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


def grades(*grade, average_situation=False):
    """
    this function analyses any number of grades and it also returns: 
        the total of grades;
        the biggest grade;
        the lowest grade;
        the medium of all grades;
        if  'average_situation' == True, it returns the situation
    """
    grade_list = list()
    for elements in grade:
        grade_list.append(elements)
    print(grade_list)
    big = grade_list[0]
    low = grade_list[0]  
    total_grades = 0  
    for current_grade in grade_list:
        if current_grade > big:
            big = current_grade
        if current_grade < low:
            low = current_grade
        total_grades += current_grade
    medium = total_grades / len(grade_list)
    result = {'total': len(grade_list), 'biggest': big, 'lowest': low, "medium": medium}
    if average_situation:
        if medium < 7:
            result['situation'] = "below average"
        elif medium == 7:
            result['situation'] = "average"
        else:
            result['situation'] = "above average"
    return result


print(area(base=2, height=5))
decoration('coding')
print(biggest(10, 2,3 , 5, 6, 11))
x = factorial(5, 3, 2, 4, 6)
print(x)
y = grades(1, 2, 3, 22, average_situation=True)
print(y)
help(grades)
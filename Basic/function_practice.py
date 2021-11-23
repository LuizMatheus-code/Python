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


def sequence(number):
    try:
        number = int(number)
        if number > 0:
            while number >= 0:
                print(number, end=' ')
                number -= 1
        elif number == 0:
            print(number)
        else:
            while number <= 0:
                print(number, end=' ')
                number += 1
    except :
        print('Error. Type a valid number')


def reverse(num):
    try:
        num = int(num)
        num = str(num)
        print(f'{num} -> ', end='')
        for digits in range((len(num) - 1), -1, -1):
            print(num[digits], end='')
    except:
        print('invalid')


def day_operation(day):
    try:
        day = int(day)
        def get_week_day(day):
            days_of_the_week = {
                1: "Sunday",
                2: 'Monday',
                3: 'Tuesday',
                4: 'Wednesday',
                5: 'Thursday',
                6: 'Friday',
                7: 'Saturday'
            }
            return days_of_the_week.get(day, 'Invalid')


        def day_search(day_to_find):
            weekend = [1, 7]
            during_the_week = [2, 3, 4, 5, 6]
            if day_to_find in weekend:
                return 'Weekend'
            elif day_to_find in during_the_week:
                return 'Day of the week'
            else:
                return 'Invalid'
        
        return f'{day}: {get_week_day(day)} ({day_search(day)})'
    except:
        return 'Invalid'


def Fibo(quantity, sequence=(0, 1)):
    return sequence if len(sequence) == quantity else \
        Fibo(quantity, sequence + (sum(sequence[-2:]), ))


def Raise(*number, percentage=0, convert=False):
    number_total = []
    raised_number = []
    for element in number:
        number_total.append(element)
    for current_number in number_total:
        current_number += (current_number * (percentage/100))
        raised_number.append(current_number)
    if convert:
        return MoneyConvert(raised_number)
    else:
        return raised_number


def Lower(*number, percentage=0, convert=False):
    number_total = []
    lowered_number = []
    for element in number:
        number_total.append(element)
    for current_number in number_total:
        current_number -= (current_number * (percentage/100))
        lowered_number.append(current_number)
    if convert:
        return MoneyConvert(lowered_number)
    else:
        return lowered_number


def Double(*number, convert=False):
    number_total = []
    doubled_number = []
    for element in number:
        number_total.append(element)
    for current_number in number_total:
        current_number *= 2
        doubled_number.append(current_number)
    if convert:
        return MoneyConvert(doubled_number)
    else:
        return doubled_number


def Half(*number, convert=False):
    number_total = []
    halved_number = []
    for element in number:
        number_total.append(element)
    for current_number in number_total:
        current_number /= 2
        halved_number.append(current_number)
    if convert:
        return MoneyConvert(halved_number)
    else:
        return halved_number


def MoneyConvert(number_list):
    converted_numbers = []
    for element in number_list:
        element = float(element)
        converted = f'R$ {element}'
        converted_numbers.append(converted)
    return converted_numbers


def Summary(value, raising=0, loweing=0):
    espace = '=' * 20 + ('=' * len(str(Double(value))))
    print(espace)
    print('Summary'.center(len(espace)))
    print(espace)
    original_value = MoneyConvert([value])[0]
    print(f'Original: \t{original_value}')
    double_value = Double(value, convert=True)
    print(f'Double: \t{double_value[0]}')
    half_of_value = Half(value, convert=True)
    print(f'Half: \t\t{half_of_value[0]}')
    raising_value = Raise(value, percentage=raising, convert=True)
    print(f'{raising}% Raised: \t{raising_value[0]}')
    lowering_value = Lower(value, percentage=loweing, convert=True)
    print(f'{loweing}% Lowered: \t{lowering_value[0]}')
    print('-' * 20 + ('-' * len(str(Double(value)))))


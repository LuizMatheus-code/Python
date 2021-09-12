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


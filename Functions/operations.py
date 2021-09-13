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


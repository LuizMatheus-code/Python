def _mdc_(x, y):
    while (y):
        x = y
        y = x % y
    return x


def mdc(numbers):
    if len(numbers) == 2:
        return _mdc_(numbers[0], numbers[1])
    else:
        mdc_value = _mdc_(numbers[0], numbers[1])
        numbers[0] = mdc_value
        del numbers[1]
        return mdc(numbers)


if __name__ == '__main__':
    print(mdc([21, 7])) #7
    print(mdc([125, 40])) #5
    print(mdc([9, 564, 66, 3])) #3
    print(mdc([55, 22])) #11
    print(mdc([15, 150])) #15
    print(mdc([7, 9])) #1

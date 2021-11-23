from random import randint

def craps_game():
    """you roll two six-sided dices and sum the result of both of them
    even: Victory (natural)
    odd: Defeat (craps)
    2, 12: +1 Point
    You need 2 points to win"""
    point = 0
    while True:
        first_dice = randint(1, 6)
        second_dice = randint(1, 6)
        sum_dices = (first_dice + second_dice)
        if sum_dices % 2 == 0:
            if sum_dices == 2 or sum_dices == 12:
                result = 'Victory by Natural'
            else:
                if point == 2:
                    result = 'Victory by points'
                    break
                point += 1
        elif sum_dices % 2 != 0:
            result = 'Defeat by craps'
            break
    print(sum_dices)
    return result


y = craps_game()
print(y)

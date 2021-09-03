money = int(input('how much money do you want in dollars? '))
total = money
banknote = 50
total_banknote = 0
while True:
    if total >= banknote:
        total -= banknote
        total_banknote += 1
    else:
        if total_banknote > 0:
            print(f'{total_banknote} of ${banknote}')
        if banknote == 50:
            banknote = 20
        elif banknote == 20:
            banknote = 10
        elif banknote == 10:
            banknote = 1
        total_banknote = 0
        if total == 0:
            break

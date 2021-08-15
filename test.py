from math import sqrt

total = []
notas = []
dado1 = 1
while True:
    dado1 = int(input("digite algo: "))
    if dado1 == 0:
        break
    else:
        dado2 = int(input("digite algo: "))
        total.append(dado1)
        total.append(dado2)

contador = 0
for item in total:
    notas.append(total[contador])
    contador += 1
    if len(notas) == 2:
        media = (notas[0] + notas[1])/2
        print("media {}: {}".format(int(contador/2), media))
        notas = []

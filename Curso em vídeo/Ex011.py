from math import ceil

#Solicitando largura da parede em float
largura_parede = float(input("Digite a largura da parede: "))

#Solicitando altura da parede em float
altura_parede = float(input("Digite a altura da parede: "))

#Calculando a área da parede ao multiplicar altura pela largura
area_parede = largura_parede * altura_parede

#Arredondando o resultado através da funcão "round", que arredonda o número para o inteiro mais próximo
area_parede = round(area_parede)

'''calculando a tinta necessária para pintar a parede
Admitindo que 1 Litro de tinta pinta 2 metros quadrados de parede'''
tinta_pintar_parede = area_parede / 2

#Arredondando a tinta necessária para pintar a parede através da funcao ceil que foi importada da biblioteca math no comeco do código
tinta_pintar_parede = ceil(tinta_pintar_parede)

#Mostrando para o usuário: largura, altura, area da parede e tinta necessária, tudo já arredondado
print('''Essa parede tem dimensão {} x {} e área {}\nPara pintar a sua parede, você precisará de {} Litros de tinta'''.format(largura_parede, altura_parede, area_parede, tinta_pintar_parede))

#Solicitando entrada de dados do tipo inteiro
numero_inserido = int(input("Digite um número inteiro: "))

#Calculando o dobro do número inserido e guardando na variável "dobro"
dobro = numero_inserido * 2

#Calculando o triplo do número inserido e guardando na variável "triplo"
triplo = numero_inserido * 3

#Calculando a raíz quadrada do número inserido e guardando na variável "raiz_quadrada"
raiz_quadrada = numero_inserido ** (1/2)

#Mostrando na tela para o usuário: o numero original, o dobro dele, o triplo e a raiz quadrada
print('''Analisando o número {}... 
O dobro é {} 
O triplo é {} 
A raíz quadrada é {:.2f}'''.format(numero_inserido, dobro, triplo, raiz_quadrada))

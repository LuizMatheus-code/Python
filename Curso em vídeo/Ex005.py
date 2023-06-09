#Solicitando entrada de dados do tipo inteiro
numero = int(input("Digite um número inteiro: "))

#Declarando variável do antecessor do número
antecessor = numero - 1

#Declarando variável do sucessor do número
sucessor = numero + 1

#Mostrando o numero inserido, o antecessor dele e também o sucessor
print("Analisando o número {}... \nO antecessor é {} \nO sucessor é {}".format(numero, numero - 1, numero + 1))

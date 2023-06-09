#Solicitando um número inteiro
numero_usado = int(input("Digite um número inteiro: "))

print("----------------")

#Através do laço de repetição "for", contando de 1 a 10
for contador in range(1, 11):
    
    #mostrando o resultado na tela 
    print("{} x {} = {}".format(numero_usado, contador, numero_usado * contador))

print("----------------")

#Solicitando a distância em metros no formato float
distancia_em_metros = float(input("Digite a distância em metros: "))

#convertendo a medida em metros para Km, para que, mais à frente, seja possível usar um laço de repetição
conversao_de_medida = distancia_em_metros / 1000

#o multiplicador é o número que será usado para fazer as multiplicações no laço de repetição
multiplicador = 1

#Esta lista existe para que seja possível usar o laço de repetição logo abaixo de forma a usar "contador" como índice
nomes_das_medidas = ["kilometro", "Decametro", "Hectometro", "Metro", "Decimetro", "Centimetro", "Milimetro"]

#O laço de repetição "For" será usado para começar da posição zero e ir até o final da lista anterior
for contador in range(0, 7):

    #O numero final é o dado que o usuário inseriu, já convertido para Km, multiplicando a variável "multiplicador" que vai aumentar depois
    numero_final = conversao_de_medida * multiplicador

    #É usado o "contador" em conjunto com a lista "nomes das medidas" para mostrar corretamente o nome da unidade de medida
    print("{}: {}".format(nomes_das_medidas[contador], numero_final))
    
    #Como o multiplicador começa como um ao ter sido declarado anteriormente, aqui, é feita uma verificação para que ele se ajuste
    if multiplicador == 1:
        #se estiver no começo, isto é: multiplicador = 1, atribuir a ele o valor 10
        multiplicador = 10
    
    else:
        #se for qualquer valor diferente de 1, isto é: já passou do começo, multiplicaro valor existente por 10
        multiplicador *= 10

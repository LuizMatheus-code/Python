#Solicitando entrada de dados em float
dinheiro_reais = float(input("Quantos reais você tem na carteira? "))

'''Realizando a conversão de real para dólar
Admitindo que USD = 4,88 R$ no dia 12/06/2023'''
reais_para_usd = dinheiro_reais / 4.88

'''Mostrando na tela: entrada de dados em reais e valor já convertido para dólar
Ambas as medidas foram aproximadas para terem apenas 2 casas decimais após a vírgula'''
print("Com R${:.2f} você pode comprar aproximadamente {:.2f} Dólares".format(dinheiro_reais, reais_para_usd))

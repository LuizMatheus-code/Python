#solicitando entrada de dados em forma de float
salario_original = float(input('Digite o valor do salario em R$: '))

#solicitando o valor das despesas em float
valor_despesas = float(input('Digite o valor das despesas em R$: '))

#calculando o percentual que foi descontado em forma inteira ao multiplicar por 100
percentual_salario = (valor_despesas / salario_original) * 100

#Mostrando na tela os valores: salario, despesas e o percentual de desconto
print('''Salario: {}
Despesas: {}
Percentual de desconto: {} 
'''.format(salario_original, valor_despesas, percentual_salario))

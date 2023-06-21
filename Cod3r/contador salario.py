#Solicitando a quantia de dinheiro em R$ do tipo float
meta = float(input('Digite a meta em R$: '))

#Solicitando o salário em R$ do tipo float
salario_bruto = float(input('Digite o salário bruto em R$: '))

#Solicitando as despesas em float
despesas = float(input('Digite as despesas do salário: '))

#calculando o salário líquido ou saldo ao subtrari as despesas do salario bruto
salario_liquido = salario_bruto - despesas

#Se o salario liquido for maior ou igual à meta, executar o código
if salario_liquido >= meta:

    #Mostrar na tela o salário líquido com só 2 casas decimais e a meta
    print("Com um saldo de {:.2f} O funcionário bateu a meta de {}".format(salario_liquido, meta))
else:
    #Pressupoe-se que, se o salario não é maior ou igual, ele só pode ser menor. Calcular a diferença entre meta e salario líquido
    quantia_pendente = meta - salario_liquido
    print("Ainda falta {} para o funcinonário bater a meta de {}".format(quantia_pendente, meta))

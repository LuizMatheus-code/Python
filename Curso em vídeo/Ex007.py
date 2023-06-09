#solicitando nome da pessoa em formato string
nome_estudante = input("digite o nome do(a) estudante: ")

#solicitando a primeira nota em formato float
primeira_nota = float(input("Digite a primeira nota: "))

#solicitando a segunda nota em formato float
segunda_nota = float(input("Digite a segunda nota: "))

#calculando a média aritmética entre as duas notas anteriores
media = (primeira_nota + segunda_nota) / 2

#mostrando na tela para o usuário: nome, primeira nota, segunda nota e média
print('''{} tirou {} e {}
Alcançando uma média de {}'''.format(nome_estudante, primeira_nota, segunda_nota, media))

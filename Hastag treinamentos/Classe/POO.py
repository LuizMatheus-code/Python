'''
Autor: Luiz Matheus
Data: 12/06/2023 
Link do tutorial: https://www.hashtagtreinamentos.com/programacao-orientada-a-objetos-python

Descricão: este script foi feito para aprender mais sobre orientacão a objetos. Criar uma classe vendedor e funcões para 
verificar se o vendedor bateu ou não a meta
'''

class Vendedor():
    #criando a classe vendedor com nome e quantidade de vendas
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0

    #a funcao "vendeu" tem como parametro as vendas realizadas
    def vendeu(self, vendas):
        self.vendas = vendas

    #Verificar se a venda é maior ou igual à meta
    def bateu_meta(self, meta):
        #se vendas for maior ou igual a meta, mostrar "Bateu a meta"
        if self.vendas >= meta:
            print(self.nome, "Bateu a meta")
        #se vendas for menor, mostrar "Não bateu a meta"
        else:
            print(self.nome, "Não bateu a meta")

kleber = Vendedor("Kleber")
kleber.vendeu(100)
kleber.bateu_meta(200)

alon = Vendedor("Alon")
alon.vendeu(100)
alon.bateu_meta(50)

class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def passar_canal(self, botao):
        if botao == "+":
            print("Aumentar o canal")
        elif botao == "-":
            print("Diminuir o canal")

controle = ControleRemoto("Preto", "10cm", "20cm", "2cm")
print(controle.altura)
controle.passar_canal("+")

class Carro:
    def __init__(self, velocidade):
        self.velocidade = velocidade
    

    def __str__(self):
        return self.velocidade


    def acelerar(self, quantidade):
        if self.velocidade >= 180:
            return None
        else:
            if quantidade + self.velocidade > 180:
                excedente = 180 - (quantidade + self.velocidade) 
                ideal = quantidade + excedente
                self.velocidade += ideal
                return self.velocidade
            else:
                self.velocidade += quantidade
                return self.velocidade


    def frear(self, quantidade):
        if self.velocidade <= 0:
            return None
        else:
            if self.velocidade - quantidade < 0:
                    self.velocidade = 0
                    return self.velocidade
            else:
                self.velocidade -= quantidade
                return self.velocidade


fusca = Carro(1)
print(fusca.velocidade)
fusca.acelerar(178)
print(fusca.velocidade)
fusca.frear(1000)
print(fusca.velocidade)

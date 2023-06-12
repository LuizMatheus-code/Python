class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_plano = ["basic", "premium"]
        if plano in self.lista_plano:
            self.plano = plano
        else:
            raise Exception("Plano inválido")
        
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_plano:
            self.plano = novo_plano
        else:
            print("Plano inválido")

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f"Ver filme {filme}")
        elif self.plano == "premium":
            print(f"Ver filme {filme}")
        elif self.plano == "basic" and plano_filme == "premium":
            print("Faça upgrade para premium antes de ver o filme")
        else:
            print("plano inválido")

cliente1 = Cliente("Fer", "Fer@fern.com", "basic")
cliente1.ver_filme("Harry Potter", "premium")

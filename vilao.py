from personagem import Personagem  # Importa a classe Personagem

class Vilao(Personagem):
    """
    A classe Vilao representa as características de um vilão no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)

    def atacar(self, alvo):
        """
        Reduz a vida de outro personagem atacado pelo vilão.
        """
        print(f'{self.nome} ataca {alvo.nome}!')
        alvo.sofrer_dano(self.ataque)

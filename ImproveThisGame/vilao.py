from personagem import Personagem  # Importa a classe Personagem

class Vilao(Personagem):
    """
    A classe Vilao representa as características de um vilão no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)
        niveis_validos = ['Baixa', 'Média', 'Alta']

    def atacar(self, alvo):
        """
        Reduz a vida de outro personagem atacado pelo vilão.
        """
        print(f'{self.nome} ataca {alvo.nome}!')
        alvo.sofrer_dano(self.ataque)

    def __str__(self):
        return f'Vilão: {self.nome}, Idade: {self.idade}, Vida: {self.vida}, Maldade: {self.maldade}'
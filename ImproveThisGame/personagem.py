class Personagem:
    """
    A classe Personagem representa um personagem genérico em um jogo.
    """
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def esta_vivo(self):
        return self.vida > 0
    
    def upgrade_vida(self, incremento=10):
        """
        Aumenta a vida do personagem. O valor padrão de incremento é 10.
        """
        self.vida += incremento
        print(f'Vida de {self.nome} após upgrade: {self.vida}')

    def sofrer_dano(self, dano):
        dano_final = max(0, dano - self.defesa)
        self.vida -= dano_final
        print(f'{self.nome} sofreu {dano_final} de dano! Vida restante: {self.vida}')
        if self.vida <=0:
            print(f'{self.nome} foi derrotado!')


    def dialogar(self, outro):
        print(f'{self.nome}: Vamos ver do que vocês são capazes {outro.nome}!')

    def __str__(self):
        return f'Personagem: {self.nome}, Idade: {self.idade}, Vida: {self.vida}'
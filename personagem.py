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
    
    def sofrer_dano(self, dano):
        dano_final = max(0, dano - self.defesa)
        self.vida -= dano_final
        print(f'{self.nome} sofreu {dano_final} de dano!')
        if self.vida <=0:
            print(f'{self.nome} foi derrotado!')

    def dialogar(self, outro):
        print(f'{self.nome}: Vamos ver do que vocês são capazes {outro.nome}!')

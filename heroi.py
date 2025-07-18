from personagem import Personagem

class Heroi(Personagem):
    '''
    A classe Heroi representa as características de um vilão no jogo.
    Herda da classe Personagem
    '''
    def __init__(self, nome, vida, ataque, defesa, pocoes=2):
        super().__init__(nome, vida, ataque, defesa)
        self.pocoes = pocoes
        self.refens_salvos = 0

    def atacar(self, alvo):
        ''' Reduz a vida de outro personagem atacado pelo herói'''
        print(f'{self.nome} ataca {alvo.nome}!')
        alvo.sofrer_dano(self.ataque)

    def usar_pocao(self):
        '''Aumenta a vida do personagem. O valor padrão de cura é 20'''
        if self.pocoes > 0:
            self.vida += 20
            self.pocoes -= 1
            print(f'{self.nome} usou uma poção de cura! Vida atual: {self.vida}')
        else: 
            print(f'Oh não! {self.nome} não tem mais poções de cura!')
    
    def salvar_refem(self):
        '''Herói salva um refém'''
        self.refens_salvos += 1
        print(f'{self.nome} salvou um refém! Total de refens salvos: {self.refens_salvos}')

import time
import random
from personagem import Personagem
from vilao import Vilao
from heroi import Heroi
from utils import Utils
from historia import mostrar_introducao

def main():
    print('-=' * 20)
    print('BEM-VINDO AO JOGO WORLD OF TAKEDOWN')
    print('-=' * 20)
    input('Pressione ENTER para iniciar a história.')
    mostrar_introducao()
    Utils.limpar_tela()
    

historico = []

heroi = random.choice(Utils.carregar_personagens("TAKEDOWN.json", Heroi))
vilao = random.choice(Utils.carregar_personagens("SystemBoys.json", Vilao))


def batalhar():
    print('🔥 Vamos começar a batalha!')
    time.sleep(2)

    heroi.dialogar(vilao)
    vilao.dialogar(heroi)

    while heroi.esta_vivo() and vilao.esta_vivo():
        Utils.exibir_status(heroi)
        Utils.exibir_status(vilao)
        acao = Utils.escolher_acao()

        if acao == '1':
            heroi.atacar(vilao)
            historico.append(f'{heroi.nome} atacaou {vilao.nome}')

    




















def main():
    # Criando personagens e vilões
    heroi = Personagem('Link', 30, 100)
    npc = Personagem('Zelda', 28, 80)
    vilao = Vilao('Ganon', 45, 120, 'Alta')

    # Mostrando personagens
    print(heroi)
    print(npc)
    print(vilao)

    # Vilão ataca o herói
    vilao.ataque(heroi)

    # Melhorando a vida do herói
    heroi.upgrade_vida(20)
    print(f'{heroi.nome} após upgrade de vida: {heroi.vida}')

    # Mudando nome do NPC
    npc.update_nome('Princesa Zelda')
    print(f'Nome atualizado: {npc.nome}')


if __name__ == "__main__":
    main()
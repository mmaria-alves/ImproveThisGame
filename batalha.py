import random
import time
from utils import Utils
from heroi import Heroi
from vilao import Vilao

historico = []

heroi = random.choice(Utils.carregar_personagens("Protagonistas/TAKEDOWN.json", Heroi))
vilao = random.choice(Utils.carregar_personagens("Protagonistas/SystemBoys.json", Vilao))

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
            historico.append(f'{heroi.nome} atacou {vilao.nome}.')
            time.sleep(1.5)
        elif acao == '2':
            heroi.usar_pocao()
            historico.append(f'{heroi.nome} usou uma poção de cura.')
            time.sleep(1.5)
        elif acao == '3':
            heroi.dialogar(vilao)
            historico.append(f"{heroi.nome} dialogou com {vilao.nome}")
            time.sleep(1.5)
        else:
            print('Opção inválida. Escolha entre 1, 2 e 3.')

        if vilao.esta_vivo():
            vilao.atacar(heroi)
            historico.append(f'{vilao.nome} atacou {heroi.nome}')
            time.sleep(2)

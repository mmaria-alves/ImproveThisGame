from utils import Utils
from historia import mostrar_introducao
from batalha import batalhar, historico

def main():
    print('-=' * 20)
    print('BEM-VINDO AO JOGO WORLD OF TAKEDOWN')
    print('-=' * 20)
    input('Pressione ENTER para iniciar a história.')
    mostrar_introducao()
    Utils.limpar_tela()
    batalhar()
    print('Deseja ver o histórico da luta? Se sim, pressione ENTER.')
    opcao = input("Se não, pressione qualquer tecla para sair.")
    if opcao == '':
        print("\n📜 Histórico de Ações:")
        for evento in historico:
            print("- " + evento)
    else:
        print('Obrigada por jogar!')


if __name__ == "__main__":
    main()

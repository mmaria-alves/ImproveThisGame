import os
import json

class Utils:
    def exibir_status(personagem):
        print(f'{personagem.nome}: Vida = {personagem.vida} | Ataque = {personagem.ataque} | Defesa = {personagem.defesa}')

    def escolher_acao():
        print('\nAções disponíveis: ')
        print('1. Atacar')
        print('2. Usar poção')
        print('3. Dialogar')
        return input('Escolha sua ação: ')
    
    def limpar_tela():
        os.system('cls' if os.name == 'nt' else 'clear')

    def carregar_personagens(caminho, classe):
        personagens = []
        try:
            with open(caminho, 'r', encoding='UTF-8') as arquivo:
                dados = json.load(arquivo)
                for item in dados:
                    personagem = classe(
                        nome = item["nome"],
                        vida = int(item["vida"]),
                        ataque = int(item["ataque"]),
                        defesa = int(item["defesa"])
                    )
                    personagens.append(personagem)
                return personagens
        except Exception as e:
            print(f'Erro ao carregar personagens {e}')
            return []

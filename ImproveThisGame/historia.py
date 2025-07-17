from utils import Utils

def mostrar_introducao():
    Utils.limpar_tela()
    historia = [
        "A Terra foi atacada e agora está lotada de seres paranormais,",
        "ameaçando a ordem e o equilíbrio do planeta.",
        "",
        "Dentre esses seres, existem os System Boys, um grupo que tem como",
        "principal objetivo instaurar ainda mais caos ao redor do globo.",
        "",
        "Entretanto, é claro que nosso mundo não ficou à mercê dos vilões.",
        "",
        "Um grupo de amigas sofreu um acidente com a queda das naves",
        "extraterrestres no mundo e acabaram se perdendo por dias numa floresta.",
        "",
        "Sem escolha, Diana, Lara, Beatrice e Luna se estabelecem naquele bosque.",
        "",
        "Depois de comer uma fruta com aparência e gosto estranho,",
        "as quatro desenvolvem poderes.",
        "",
        "Ao ver o que havia acontecido com o resto do planeta,",
        "elas adotam o nome de TAKEDOWN.",
        "",
        "Agora, o objetivo principal delas é salvar as pessoas restantes,",
        "enquanto tentam entender e se acostumar com suas novas habilidades.",
        "",
        "Prepare-se para entrar nessa aventura!"
    ]
    for trecho in historia:
        print(trecho)
        input('Pressione ENTER para continuar...')

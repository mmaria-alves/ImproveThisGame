from utils import Utils

def mostrar_introducao():
    Utils.limpar_tela()
    introducao = [
        "A Terra foi atacada e agora está lotada de seres paranormais, ameaçando a ordem e o equilíbrio do planeta.",
        "Dentre esses seres, existem os System Boys, um grupo que tem como principal objetivo instaurar ainda mais caos\nao redor do globo.",
        "Entretanto, é claro que nosso mundo não ficou à mercê dos vilões.",
        "..."
        "Um grupo de amigas sofreu um acidente com a queda das naves extraterrestres no mundo e acabaram ficando presas\npor dias numa floresta.",
        "Sem escolha, Diana, Lara, Beatrice e Luna se estabeleceram naquele bosque enquanto esperavam pelo resgate.",
        "Mas, depois de comer uma fruta com aparência e gosto estranho, as quatro desenvolvem poderes e foram capazes\nde sair, por conta própria, daquela matagal.",
        "E, ao ver o que havia acontecido com o resto do planeta, elas decidiram usar seus poderes para salvar as pessoas\nque restaram",
        "Adotando o nome de TAKEDOWN, tudo isso enquanto tentam entender e se acostumar com suas novas habilidades.",
        "Prepare-se para entrar nessa aventura!"
    ]
    for trecho in introducao:
        print(trecho)
        input('Pressione ENTER para continuar...\n')

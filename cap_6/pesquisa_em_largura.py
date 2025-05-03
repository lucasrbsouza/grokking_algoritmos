from collections import deque

grafo = {
    "você": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}


def pessoa_e_vendedor(nome):
    return nome[-1] == 'y'


def pesquisa_em_largura(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = []

    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(pessoa + " é um vendedor de manga")
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)
    print("Nenhum vendedor de manga encontrado")
    return False


if __name__ == '__main__':
    grafo = {"você": ["alice", "bob", "claire"], "bob": ["anuj", "peggy"], "alice": ["peggy"],
             "claire": ["thom", "jonny"],
             "anuj": [], "peggy": [], "thom": [], "jonny": []}

    pesquisa_em_largura("você")

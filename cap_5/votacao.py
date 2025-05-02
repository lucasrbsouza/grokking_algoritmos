votaram = {}


def isVotou(nome):
    if votaram.get(nome.lower()):
        print("vai te embora macho")
    else:
        votaram[nome.lower()] = True
        print("Deixe votar")


def mostrar_lista():
    print(votaram)


isVotou("Lucas")
mostrar_lista()
isVotou("Lucas")

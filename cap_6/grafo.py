"""num grafo não importa a ordem que os ‘items’ são adicionados,
pois uma tabela hash não são ordenadas
"""
grafo = {}

grafo["você"] = ["alice", "bob", "claire"]

grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []

print(grafo)

Função BFS(Grafo G, Vértice s):
    Crie uma fila Q
    Marque s como visitado
    Enfileire s em Q

    Enquanto Q não estiver vazia:
        v ← Desenfileire Q
        Para cada vizinho w de v:
            Se w não foi visitado:
                Marque w como visitado
                Enfileire w em Q

# Fatorial

def fat(num):
    if num == 1: # caso base
        return 1
    else: # caso recursivo
        """ antes de ser resolvido a mutiplicacao
            será feita a recursao do numero - 1
            ex: 
                num = 4 -> 4 -1 = 3
                num = 3 -> 3-1 = 2
                num = 2 -> 2-1 = 1
                num = 1 -> retorna 1
            e depos será resolvido recursivamento a pilha de chamada
            ex:
                1 * 1 = 1
                2 * 1 = 2
                3 * 2 = 6
                4 * 6 = 24
        """
        return num * fat(num - 1)

# numero em regressao

def regressiva(num):
    print(num)
    if num == 1:
        return
    else:
        """
             ex:
                num = 4 -> 4 -1 = 3
                num = 3 -> 3-1 = 2
                num = 2 -> 2-1 = 1
                num = 1 -> retorna 1
                    
             ex:
                1 + 1 = 2
                2 + 1 = 2
                3 + 2 = 6
                4 + 6 = 24
        """
        regressiva(num - 1)

if __name__ == "__main__":
    regressiva(5)
    print("*"*40)
    print(fat(4))

def soma(lista):
    # caso base:
    if lista == []:
        return 0
    return lista[0] + soma(lista[1:])

def conta(lista):
    if lista == []:
        return 0
    return 1 + conta(lista[1:])

lista = [1,2,3,4,5,6,7,8,9,10]
print(soma(lista))
print(conta(lista))
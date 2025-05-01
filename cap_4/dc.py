def soma(lista):
    if lista == []:
        return 0
    return lista[0] + soma(lista[1:])

def conta(lista):
    if lista == []:
        return 0
    return 1 + conta(lista[1:])

def max(lista):
    if len(lista) == 2:
        return lista[0] if lista[0]>lista[1] else lista[1]
    sub_max = max(lista[1:])
    return lista[0] if lista[0]> sub_max else sub_max

if __name__ == "__main__":
    lista = [1,2,3]
    suma = 1 + len(lista[1:])

    print(soma(lista))
    print(conta(lista))
    print(max(lista))
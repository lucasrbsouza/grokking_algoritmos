def fat(num):
    #primeiro o caso base
    if num == 1:
        return 1
    #depois o caso recursivo
    else:
        return num * fat(num-1)

def regressa_numerica(num):
    print(f'{num}!')
    if num == 1:
        return
    else:
        regressa_numerica(num - 1)

if __name__ == "__main__":

    num = 5

    regressa_numerica(num)
    print("-"*20)
    print(fat(num))

def fat(n):
    # primeiro o caso base
    if n == 1:
        return 1
    # depois o caso recursivo
    else:
        return n * fat(n-1)

if __name__ == "__main__":
    print(fat(5))
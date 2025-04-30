def regressiva(i):
    print(i)
    if i>0:
        regressiva(i-1)
    else:
        return

if __name__ == '__main__':
    regressiva(10)
def fat(n):
    if n == 1:
        return 1
    else:
        return n * fat(n-1)
if __name__ == "__main__":
    print(fat(5))
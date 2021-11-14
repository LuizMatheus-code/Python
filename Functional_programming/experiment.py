def factor(n):
    return n * (factor(n -1) if (n - 1) > 1 else 1)


if __name__ == '__main__':
    print(factor(5))

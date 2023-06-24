from functools import reduce

def fatorial(n):
    lista = [items for items in range(1, n + 1)]
    resultado = reduce(lambda x, y: x * y, lista)
    return resultado

if __name__ == "__main__":
    print(f'10! = {fatorial(6)}')

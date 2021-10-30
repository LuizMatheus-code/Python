import csv
from urllib import request


def read(url):
    with request.urlopen(url) as filein:
        print('download due')
        data = filein.read().decode('latin1')
        print('download done')
        for city in csv.reader(data.splitlines()):
            print(f'{city[8]}: {city[3]}')


if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')

'''
Autor: Luiz Matheus
Data: 23/06/2023
Descricão: Este programa pergunta se dois trabalhos foram feitos. Com base nos trabalhos feitos, ele retorna se a pessoa pode comprar
uma televisão nova ou um sorvete ou até os dois. Existem verificações para assegurar que as respostas sejam aplicáveis.
'''

print("O trabalho a ser realizado na terça foi feito?")
print('''[1] Sim \n[2] Não''')

#esta variável vai contar o número de vezes que o trabalho foi concluído
trabalhos_feitos = 0

#aqui, será armazenado ou o número 1 ou 2, se não forem esses, haverá uma verificação mais à frente
primeira_resposta = input("Resposta: ").strip()

#É feita uma tentativa de converter a resposta em string para um número inteiro
try:
    #Aqui é feita a conversão para inteiro
    primeira_resposta = int(primeira_resposta)

    #Se a resposta for 1 ou 2, então é acionado o código
    if primeira_resposta == 1 or primeira_resposta == 2:
        
        #Se a resposta foi 1, então o trabalho foi feito e será armazenado na variável "trabalhos_feitos" 
        if primeira_resposta == 1:
            trabalhos_feitos += 1
        
        print("\nO trabalho da quinta foi feito?")
        print('''[1] Sim \n[2] Não''')

        #Solicitando a segunda resposta que deve ser ou 1 ou 2 e, se não for, o programa será interrompido
        segunda_resposta = input("Resposta: ").strip()

        #Aqui, é feita a tentativa de converter a resposta em string para número inteiro
        try:
            segunda_resposta = int(segunda_resposta)

            #A resposta só vai passar se foi 1 ou 2
            if segunda_resposta == 1 or segunda_resposta == 2:

                #Se a resposta foi 1, então o trabalho foi feito e será armazenado na variável "trabalhos_feitos"
                if segunda_resposta == 1:
                    trabalhos_feitos += 1
            else:

                #Este bloco só vai acontecer se a resposta for um número que não é nem 1 nem 2
                print("resposta inválida")
        except:
            
            #Este bloco só acontece se a resposta da variável "segunda_resposta" foi um tipo que não se converte para número inteiro
            print("A resposta precisa ser um número")
    else:

        #Este bloco só acontece se a resposta da variável "primeira_resposta" não for nem 1 nem 2
        print("resposta inválida")
except:

    #Este bloco é ativado quando a resposta da variável "primeira_resposta" não é um tipo que se converte para número inteiro
    print("A resposta precisa ser um número")

#Este bloco é acionado independente das verificações anteriores
finally:
    print('\nProcessando resposta...')

#Se os dois trabalhos foram feitos, então este código será acionado
if trabalhos_feitos == 2:
    print("{} Trabalhos concluidos \nPode comprar uma televisão nova e um sorvete".format(trabalhos_feitos))

#Se apenas um trabalho foi feito, então este código será acionado
elif trabalhos_feitos == 1:
    print('{} Trabalho concluido \nPode comprar só o sorvete'.format(trabalhos_feitos))

#Se nenhum trabalho foi feito, ou se as respostas anteriores não passaram na verificação, então este bloco será acionado
else:
    print('Nenhum trabalho foi concluido')

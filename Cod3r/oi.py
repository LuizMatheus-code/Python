print("O trabalho a ser realizado na terça foi feito?")
print('''[1] Sim
[2] Não''')

primeira_resposta = input("Resposta: ")

try:
    primeira_resposta = int(primeira_resposta)

    if primeira_resposta == 1 or primeira_resposta == 2:
        print("\nO trabalho da quinta foi feito?")
        print('''[1] Sim \n[2] Não''')

        segunda_resposta = input("Resposta: ")

        try:
            segunda_resposta = int(segunda_resposta)
            if primeira_resposta == 1 and segunda_resposta == 2:
                pass

            else:
                print("resposta inválida")
        except:
            pass
    else:
        print("resposta inválida")
except:
    pass

'''
try:

except:

else:

finally:
'''
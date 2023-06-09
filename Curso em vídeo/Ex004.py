#Solicitando dados do usuário
palavra_usada = input("Digite uma palavra: ")

#Declarando uma variável para guardar tipo primitivo dos dados inseridos
tipo_primitivo = type(palavra_usada)
#Mostrando ao usuário a palavra usada e o tipo primitivo dela
print("O tipo primitivo de {} é {}".format(palavra_usada, tipo_primitivo))


#Verificando se a palavra usada é formada somente de espacos
Verificar_espacos = palavra_usada.isspace()
#Mostrando na tela o resultado da verificação anterior
print("Formado só de espaços?", Verificar_espacos)


#Verificando se a palavra é formada somente de números
Somente_numero = palavra_usada.isnumeric()
#Mostrando na tela
print("{} é apenas númerico? {}".format(palavra_usada, Somente_numero))


#Verificando se a palavra é formada somente de letras
verificar_alfabetico = palavra_usada.isalpha()
#Mostrando na tela
print("{} é formado apenas por letras? {}".format(palavra_usada, verificar_alfabetico))


#Verificando se é alfanumérico
verificar_alfanumerico = palavra_usada.isalnum()
#Mostrando na tela
print("{} é formado por números ou letras? {}".format(palavra_usada, verificar_alfanumerico))


#Verificando se é fomrado somente por letras maiúsculas
verificar_maiusculas = palavra_usada.isupper()
#Mostrando na tela
print("{} é formado apenas de letras maiúsculas? {}".format(palavra_usada, verificar_maiusculas))


#Verificando se é formado somente por letras minúsculas
verificar_minusculas = palavra_usada.islower()
#Mostrando na tela
print("{} é formado apenas de letras minúsculas? {}".format(palavra_usada, verificar_minusculas))


#Verificando se a palavra inicia com letra maiúscula
verificar_capitalizada = palavra_usada.istitle()
#Mostrando na tela
print("{} inicia com letra maiúscula? {}".format(palavra_usada, verificar_capitalizada))

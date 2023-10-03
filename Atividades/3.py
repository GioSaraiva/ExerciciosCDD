'''CRIE UM CÓDIGO QUE LEIA A IDADE DE  UMA PESSOA E DIGA EM QUAL ANO ELA NASCEU'''

idade=int(input('Qual a sua idade: '))
mesnasc= int(input('De 1 a 12, qual o mês que você nasceu? '))
mesatual=int(input('qual o mês que você está? '))
calculo= 2023-idade
if mesnasc > mesatual:
    print(calculo - 1)
else:
    print(calculo)
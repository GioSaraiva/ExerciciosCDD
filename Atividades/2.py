'''CRIE UM CÓDIGO QUE LEIA UM NÚMERO DIFERENTE DE ZERO E DIGA SE ESTE NÚMERO É POSITIVO OU NEGATIVO'''

num= int(input('Digite um número diferente de 0:'))
while num==0:
    num = int(input('Digite um número diferente de 0:'))
if num%2==0:
    print('Número par.')
else:
    print('Número é impar.')
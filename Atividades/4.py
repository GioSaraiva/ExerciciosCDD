'''Crie um algoritmo que receba 3 números e informe qual o maior entre eles.'''

num1=int(input('Digite um numero: '))
num2=int(input('Digite um numero: '))
num3=int(input('Digite um numero: '))
if num1>num2:
 if num1>num3:
    print(f'O número {num1} é o maior! ')
elif   num2>num3:
    print(f'O número {num2} é o maior!')
else:
    print(f'O número {num3} é o maior!')
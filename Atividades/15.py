'''Escreva um algoritmo para ler dois
valores (considere que não serão lidos
valores iguais) e escrevê-los em ordem
crescente'''

num1 = int(input("INFORME UM VALOR: "))
num2 = int(input("INFORME UM VALOR: "))
while num1 == num2:
    num2 = int(input("NUMERO IGUAL, INFORME UM VALOR: "))

if num1 < num2:
        print(f"{num1},{num2}")
else:
    print(f"{num2},{num1}")
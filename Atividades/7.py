'''Faça um código que receba o valor da base e da altura de um triângulo e calcule sua área usando a fórmula
A= (base x altura) / 2 e que não aceite o número (0), na base e na altura'''

base = float(input("DIGITE A BASE: "))
while base == 0:
    base = float(input("NUMERO IGUAL A 0, DIGITE NOVAMENTE A BASE: "))
altura = float(input("DIGITE A ALTURA: "))
while altura == 0:
    altura = float(input("NUMERO IGUAL A 0, DIGITE A ALTURA: "))
area = (base * altura) / 2
print(f"A AREA DO TRIANGULO: {area}")
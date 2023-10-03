'''Faça um algoritmo que leia a idade de
uma pessoa expressa em anos, meses e dias
e escreva a idade dessa pessoa expressa
apenas em dias. Considerar ano com 365
dias e mês com 30 dias'''

ano = int(input("Escreva sua idade: "))
meses = int(input("Escreva mês que você nasceu: "))
dias = int(input("Escreva o dia que você nasceu: "))

diatotal= (ano*365)+(meses*30)+dias

print(f"Sua idade em dias é: {diatotal}!")
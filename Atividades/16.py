'''Escreva um algoritmo para ler a hora de
início e a hora de fim de um jogo de Xadrez
(considere apenas horas inteiras, sem os
minutos) e calcule a duração do jogo em
horas, sabendo-se que o tempo máximo de
duração do jogo é de 24 horas e que o jogo
pode iniciar em um dia e terminar no dia
seguinte'''
horainicio= int(input("INFORME A HORA DE INICIO: "))
horafim = int(input("INFORME A HORA DO FIM: "))

if horainicio >= horafim:
    duracao= 24 - horainicio+horafim
    print(f"A DURAÇÂO DO JOGO FOI DE {duracao} HORAS ")
else:
    duracao = horafim-horainicio
    print(f"A DURAÇÂO DO JOGO FOI DE {duracao} HORAS ")
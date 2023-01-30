"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_str = input('Digite um número inteiro: ')

try:
    numero_int = int(numero_str)
    if (numero_int % 2 == 0):
        print('Esse número é par')
    else:
        print('Esse número é ímpar')
except:
    print('Você não digitou um número inteiro')   


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_usuario = input('Que horas são, em números inteiros? ')

try:
    hora = int(hora_usuario)
    manha = (hora >=0 and hora <=11)
    tarde = (hora >=12 and hora <=17)
    noite = (hora >=18 and hora <=23) #Desnecessário

    if manha:
        print('Bom dia!')
    elif tarde:
        print('Boa tarde')
    elif noite:
        print('Boa noite')
    else:
        print('Você mão digitou uma hora válida! (de 0 a 23h)')
except:
    print('Você não digitou um valor válido (inteiro)')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""


nome_usuario = input('Qual o seu primeiro nome? ')
tamanho_nome = len(nome_usuario)

nome_curto = tamanho_nome <= 4
nome_normal = tamanho_nome > 4 and tamanho_nome <=6

if nome_curto:
    print('Seu nome é curto')
elif nome_normal:
    print('Seu nome é normal')
else:
    print("Seu nome é grande")

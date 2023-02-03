"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os
#os.system('cls')
lista = []

while True:
    print('Selecione uma opção')
    option = input('[i]nserir [a]pagar [l]istar: ')

    if (len(option) > 1):
        print('Opção Inválida!')
        continue

    for letra in option:
        if (letra not in 'ial'):
            print('Opção Inválida!')
            continue


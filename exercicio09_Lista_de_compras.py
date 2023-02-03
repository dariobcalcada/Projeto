"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

#import os

lista = []

while True:
    print('Selecione uma opção')
    option = input('[i]nserir [a]pagar [l]istar: ')

    for letra in option:
        
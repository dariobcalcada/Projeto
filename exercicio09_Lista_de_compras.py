"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os
#os.system('cls')
lista = ['teste', 'teste2']

while True:
    print('Selecione uma opção')
    option = input('[i]nserir [a]pagar [l]istar: ')

    if (len(option) > 1): #Se digitou mais de um caracter na opção
        os.system('cls')
        print('Opção Inválida!')
        continue

    for letra in option:
        if (letra not in 'ial'): #digitou apenas 1 caracter mas não é umas das opções
            os.system('cls')
            print('Opção Inválida!')
            continue

    if (option == 'l'): #OPÇÃO DE LISTAR A LISTA
        if (len(lista) == 0): #LISTA VAZIA
            os.system('cls')
            print('A lista está vazia!')
            continue
        else:
            os.system('cls')
            for indice, nome in enumerate(lista):
                print(indice, nome) #TESTE print(indice, nome, lista[indice])
                continue
    elif (option == 'a'): #OPÇÃO DE APAGAR ITEM NA LISTA
        if (len(lista) == 0): #LISTA VAZIA
            os.system('cls')
            print('A lista está vazia!')
            continue
        else:
            os.system('cls')
            posicao = input('Escolha o índice que deseja apagar: ')
            
            try: #garantir que o índice é um inteiro
                pos = int(posicao)
            except:
                print('Posição inválida!')
                continue        
            
            if (pos <0) or (pos >= len(lista)):
                print('Posição inválida!')
                continue
            else:
                del lista[pos]
                print('Item apagado como sucesso')
                continue
    else:
        #INSERIR ITEM NA LISTA
        item_novo = input('Digite o item que deseja inserir: ')
        lista.append(item_novo)
        print('Item adicionado com sucesso!')
        continue

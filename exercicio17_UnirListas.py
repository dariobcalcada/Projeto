# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest


def zipper (lista_um,lista_dois):
    tamanho_menor = min(len(lista_um),len(lista_dois))
    return [
       (lista_um[i], lista_dois[i]) for i in range(tamanho_menor)

    ]


l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(l1,l2))

## FUNÇÃO EM PYTHON QUE JÁ FAZ A UNIÃO DE LISTAS PELA MENOR
print(list(zip(l1,l2)))

## FUNÇÃO EM PYTHON QUE FAZ A UNIÃO DE LISTAS PELA MAIOR ACRESCENTANDO ITENS (fillvalue) ---> Necessita importar pacote itertools

print(list(zip_longest(l1,l2, fillvalue='SEM VALOR CORRESPONDENTE')))
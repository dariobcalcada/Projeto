"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

conta_lista = range(len(lista))

for indice in conta_lista:
    print(indice, lista[indice], type(lista[indice]))
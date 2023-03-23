import copy


# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

print('*** Essa é a lista de produtos original ***')
print(produtos)
print()
print()


produtos_mais_dez = copy.deepcopy(produtos)

for produto in produtos_mais_dez:
    preco = produto.get('preco')
    preco *= 1.1
    produto['preco'] = preco
    
print('*** Essa é a lista de produtos com aumento de 10% no preço ***')
print(produtos_mais_dez)
print()
print()

produtos_nome_decrescente = sorted(copy.deepcopy(produtos), key=lambda k: k['nome'], reverse=True)


print('*** Essa é a lista de produtos na ordem descrescente do nome ***')
print(produtos_nome_decrescente)
print()
print()


produtos_preco_cresc = sorted(copy.deepcopy(produtos), key=lambda k: k['preco'])

print('*** Essa é a lista de produtos na ordem crescente do preço ***')
print(produtos_preco_cresc)
print()
print()



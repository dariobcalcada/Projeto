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

produtos_mais_dez = produtos



produtos_preco_cresc = produtos

for produto in produtos_mais_dez:
    preco = produto.get('preco')
    preco *= 1.1
    produto['preco'] = preco
    
print('*** Essa é a lista de produtos com aumento de 10% no preço ***')
print(produtos_mais_dez)
print()
print()

produtos_nome_decrescente = produtos
produtos_nome_decrescente = sorted(produtos)

print(produtos_nome_decrescente)






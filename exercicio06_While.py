nome = 'Dario Brito Calçada'

tamanho_nome = len(nome)

print(nome)
print(tamanho_nome)

novo_nome = ''
i = 0

while i < tamanho_nome:
    novo_nome += f'{nome[i]}*'
    i += 1

print(novo_nome)

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)
idade = input('Digite sua idade: ')
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[-1:-1-tamanho_nome:-1]}')
    #print(f'Seu nome invertido é {nome[::-1]}') outra possibilidade com índice negativo
    print(f'Você tem {idade} anos de idade')
    if ' ' in nome:
        print(f'Seu nome contem espaços')
        #print(f'Seu nome tem {tamanho_nome1} letras')
    else:
        print(f'Seu nome não contem espaços')
        #print(f'Seu nome tem {tamanho_nome} letras')
    print(f'Seu nome tem {tamanho_nome} caracteres com os espaços')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[tamanho_nome-1]}')
    # print(f'A última letra do seu nome é {nome[-1]}') outra possibilidade com o índice negativo
else:
    print('Desculpe, mas você deixou campos vazios')

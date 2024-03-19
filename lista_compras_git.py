# Importar a biblioteca os
import os

# Criar minha lista vazia (a ser preenchida)
lista = []

# Tudo vai acontecer dentro do while, para que se repita infinitamente
while True:
    opcao = input('Digite uma opção:\n[i]nserir um item\n[a]pagar um item\n[l]istar elementos\n ---> ')
    opcao = opcao.lower()

    if opcao == 'i':
        os.system('cls') # Esse comando faz limpar a tela

        item = input('Digite o item a ser adicionado --> ')
        lista.append(item)

    elif opcao == 'a':
        
        # Aqui vou criar uma lista enumerada para listar os itens. Em seguida o usuário escolhe o item a ser deletado
        lista_enumerada = enumerate(lista)
        for i in lista_enumerada:
            print(i)
        item_apagar = input('Digite o índice correspondente ao item a ser apagado --> ')

        try:            
            item_apagar = int(item_apagar)
            del lista[item_apagar]

        except ValueError:
            print('Digite corretamente')
        
        except IndexError:
            print('Digite corretamente')

    elif opcao == 'l':
        lista_enumerada = enumerate(lista)
        for i in lista_enumerada:
            print(i)

    else: 
        print('Valor não encontrado!')
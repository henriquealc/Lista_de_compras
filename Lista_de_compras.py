import os
lista = [] # Sempre criar a variavel lista fora da estrutura de repetição

print('{:^30}'.format('========== Mercado =========='))
while True:
    opcao = input('Selecione uma opção: \n[i]nserir [a]apagar [l]istar s[air]: ').lower()
    if opcao == 'i':
        os.system('cls')
        inserir = input('Valor: ')
        lista.append(inserir)
    elif opcao == 'a':
        os.system('cls')
        apagar = input('Digite o indice que deseja apagar: ')
        
        try:
            indice = int(apagar)
            del lista[indice] # deletar um indice da lista
        
         # informa o erro
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')
        print(lista) # Informa a lista e os itens que contém nela
        
        if len(lista) == 0:
            print('Nada para listar')
        
        for i, valor in enumerate(lista):
            print(i, valor)
        # mostra os indices da lista
    elif opcao == 's':
        print('Programa encerrado com sucesso, Obrigado!')
        break
    else:
        print('Por favor escolha i, a ou l.')
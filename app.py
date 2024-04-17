from os import system

restaurantes = []

def exibir_nome_do_programa():
    print("A casa da vóvó\n")

def espaco():
    print('-'*25)

def exibir_opcoes():
    espaco()
    print("""1. Cadastrar Restaurante

2. Listar restaurante

3. Ativar  restaurante

4. sair""")
    espaco()

def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar o menu principal\n') 
    main()

def cadastrar_novo_restaurante():
    system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Nome do Restaurante para cadastro: ')
    restaurantes.append(nome_do_restaurante)
    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    input('Digite uma tecla para voltar ao menu principal\n')
    main()
    
    pass

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                print('Listar Restaurantes')
            case 3:
                print('Ativar Restaurante')
            case 4:
                finalizar_app()
    except:
        opcao_invalida()

def finalizar_app():
    system('cls')
    print('Finalizando o App')

def main():
    system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
if __name__ == '__main__':
    main()
    

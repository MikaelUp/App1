from os import system

restaurantes = [{'nome': 'praça', 'categoria': 'japonesa', 'ativo':False},
                 {'nome' : 'Pizza', 'categoria': 'itlaizana',
                  'ativo':True}
]

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
    system('cls')
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal\n')
    main()

def exibir_subtitulo(texto):
    system('cls')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Nome do Restaurante para cadastro: ')
    categoria = input(f"""Digite o nome da categoria do restaurante
{nome_do_restaurante}: """)
    dados_do_restaurante = {'nome': nome_do_restaurante,
    'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'{nome_restaurante} | {categoria} | {ativo}\n')

    
    voltar_ao_menu_principal()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar Restaurante')
            case 4:
                finalizar_app()
    except:
        opcao_invalida()

def finalizar_app():
    exibir_subtitulo('Finalizando o App')

def main():
    system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
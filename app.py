# Importação das bibliotecas necessárias
from os import system  # Importa apenas a função 'system' do módulo 'os'

# Lista de restaurantes
restaurantes = [{'nome': 'praça', 'categoria': 'japonesa', 'ativo': False},
                {'nome': 'Pizza', 'categoria': 'italiana', 'ativo': True}
]

# Função para exibir o nome do programa
def exibir_nome_do_programa():
    print("A casa da vóvó\n")

# Função para imprimir uma linha separadora
def espaco():
    print('-' * 25)

# Função para exibir as opções disponíveis no menu principal
def exibir_opcoes():
    espaco()
    print("""1. Cadastrar Restaurante
2. Listar restaurante
3. Ativar  restaurante
4. Sair""")
    espaco()

# Função para lidar com opções inválidas
def opcao_invalida():
    system('cls')
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

# Função para voltar ao menu principal
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal\n')
    main()

# Função para exibir um subtítulo
def exibir_subtitulo(texto):
    system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

# Função para cadastrar um novo restaurante
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Nome do Restaurante para cadastro: ')
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {'nome': nome_do_restaurante,
                            'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

# Função para listar os restaurantes
def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    print(f'{"Nome do Restaurante".ljust(20)} | {"Categoria".ljust(20)} | {"Status"}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

# Função para alternar o estado de um restaurante
def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'\nO restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'\nO restaurante {nome_restaurante} foi desativado com sucesso.'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()

# Função para escolher as opções
def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
    except:
        opcao_invalida()

# Função para finalizar o programa
def finalizar_app():
    exibir_subtitulo('Finalizando o App')

# Função principal
def main():
    system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

# Verifica se o programa está sendo executado como o principal
if __name__ == '__main__':
    main()

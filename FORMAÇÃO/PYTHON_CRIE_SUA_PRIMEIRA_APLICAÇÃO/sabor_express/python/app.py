import os

restaurantes = [
    {
        'nome': 'McDonalds',
        'categoria': 'FastFood',
        'status': False
    },
    {
        'nome': 'Madero',
        'categoria': 'Hamburgueria',
        'status': True
    },
    {
        'nome': 'Casa do Sushi',
        'categoria': 'Japonês',
        'status': False
    },
]

def exibir_nome_do_app():
    '''Essa função exibe o nome do App no terminal.'''
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    ''')

def exibir_opcoes():
    '''Essa função é responsável por exibir as opções de ações que o usuário pode fazer no App.'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def finalizar_programa():
    '''Essa função é responsável por informar ao usuário que o programa foi finalizado.'''
    exibir_subtitulo('Finalizando o App...')

def voltar_ao_menu():
    '''Essa função faz com que o usuario, digitanto qualquer tecla, volte ao menu de opções.'''
    input('\nDigite uma tecla para voltar para o menu principal ')
    main()

def opcao_invalida():
    '''Essa função exibe uma mensagem de que a opção não existe, e volta ao menu principal.'''
    print('Opção inválida!')
    voltar_ao_menu()

def exibir_subtitulo(texto):
    '''Essa função recebe um texto (str) como parâmetro e: 
    
    1. Limpa o terminal 
    2. Exibe o texto recibido 
    3. Coloca um espaçamento
    
    '''
    os.system('cls') #? Se for MAC → os.system('clear')
    print(texto)
    print('')

def cadastrar_novo_restaurante():
    '''Essa função cadastra um novo restaurante no App.
    
    Inputs:
    - Nome do restaute
    - Categoria do restaurante

    Status é um default `False`
    
    Output:
    - Insere o novo restaurante no dicionário `restaurantes`
    '''
    exibir_subtitulo('''
█▀▀ ▄▀█ █▀▄ ▄▀█ █▀ ▀█▀ █▀█ █▀█   █▀▄ █▀▀   █▄░█ █▀█ █░█ █▀█ █▀   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀ █▀
█▄▄ █▀█ █▄▀ █▀█ ▄█ ░█░ █▀▄ █▄█   █▄▀ ██▄   █░▀█ █▄█ ▀▄▀ █▄█ ▄█   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄ ▄█
''')
    nome_do_restaurante = input('\nDigite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Qual categoria o restaurante {nome_do_restaurante} pertence? ')

    dados_do_restaurante = {
        'nome': nome_do_restaurante,
        'categoria': categoria,
        'ativo': False
    }

    restaurantes.append(dados_do_restaurante)

    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu()

def listar_restaurantes():
    '''Essa função é responsável por exibir todos os restaurantes cadastrados, no dicionario `restaurantes`, no terminal para o usuário, em forma de tabela. 
    
    Exibe:
    - Nome
    - Categoria
    - Status 
    
    Aqui também é trocado o status de `True` para Ativado e `False` para Desativado.
    '''
    exibir_subtitulo('''
█░░ █ █▀ ▀█▀ ▄▀█ █▄░█ █▀▄ █▀█   █▀█ █▀   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀ █▀
█▄▄ █ ▄█ ░█░ █▀█ █░▀█ █▄▀ █▄█   █▄█ ▄█   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄ ▄█
''')

    print(f'{'----------------------'.ljust(22)} | {'--------------------'.ljust(20)} | ------------' ) 
    print(f'{'NOME DO RESTAURANTE'.ljust(22)} | {'CATEGORIA'.ljust(20)} | STATUS')
    print(f'{'----------------------'.ljust(22)} | {'--------------------'.ljust(20)} | ------------' ) 
    for restaurante in restaurantes:
        nome_do_restaurante = restaurante['nome']
        categoria_do_restaurante = restaurante['categoria']
        status_do_restaurante = 'Ativado' if restaurante['status'] else 'Desativado'
        print(f"• {nome_do_restaurante.ljust(20)} | {categoria_do_restaurante.ljust(20)} | {status_do_restaurante}")

    voltar_ao_menu()

def alterar_status_restaurantes():
    '''Essa função altera o status do restaurante no App. 
    
    Inputs:
    - Nome do restaurante 
    
    Se:
    - O restaurante estiver no dicionário `resturantes`, o status é alterado para o oposto de seu valor
    - Se for `True` vira `False`, e se for `False` vira `True`. 
    
    Se não:
    - Exibe no terminal a mensagem de que não foi encontrado.
    '''
    exibir_subtitulo('''
▄▀█ █░░ ▀█▀ █▀▀ █▀█ ▄▀█ █▀█   █▀ ▀█▀ ▄▀█ ▀█▀ █░█ █▀   █▀▄ █▀█   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀
█▀█ █▄▄ ░█░ ██▄ █▀▄ █▀█ █▀▄   ▄█ ░█░ █▀█ ░█░ █▄█ ▄█   █▄▀ █▄█   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄
''')
    
    nome_do_restaurante = input('Qual o nome do restaurante que deseja alterar o status? \n\nDigite: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['status'] = not restaurante['status']
            mensagem = f'\nO restaurante {nome_do_restaurante} foi ativado com sucesso!' if restaurante['status'] else f'\nO restaurante {nome_do_restaurante} foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print(f'\nO restaurante {nome_do_restaurante} não foi encontrado!')

    voltar_ao_menu()

def escolher_opcao():
    '''Essa função determina as funções que serão chamadas quando o usuário escolhe uma das opções.
    
    Input:
    - Número (`int`)
    
    Condição:
    - Caso o usuário digite um número que não corresponda a nenhuma das opções a função `opção_invalida()` é chamada.
    - Se o usuáro digitar uma letra, a a função `opção_invalida()` também é chamada.
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_status_restaurantes()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Essa é a função principal do programa. 
    
    Funcionalidades:
    - Limpa o terminal
    - Exibe o nome do App
    - Mostra as opções de ação do usuário
    - Possibilita que o usuário escolha uma das opções.
    '''
    os.system('cls')
    exibir_nome_do_app()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

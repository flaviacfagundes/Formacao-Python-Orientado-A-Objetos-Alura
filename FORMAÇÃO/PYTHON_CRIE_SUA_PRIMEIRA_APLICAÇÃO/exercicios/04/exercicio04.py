
#? EXERCICIO 01

pessoas = [
    {
        'nome': 'Flávia',
        'idade': 20,
        'cidade': 'Curitiba',
        'profissao': ''
    },
    {
        'nome': 'Maria',
        'idade': 80,
        'cidade': 'Astorga',
        'profissao': ''
    },
    {
        'nome': 'Isabel',
        'idade': 46,
        'cidade': 'São Jorge do Patrocinio',
        'profissao': ''
    }
]

print('')
for pessoa in pessoas:
    nome = pessoa['nome']
    idade = pessoa['idade']
    cidade = pessoa['cidade']
    print(f'• Nome: {nome} | Idade: {idade} | Cidade: {cidade}')

#? EXERCICIO 02

print('')

nome_pessoa = input('\nQual o nome da pessoa que você gostaria de alterar a idade? \n\nDigite aqui: ')

for pessoa in pessoas:
    if pessoa['nome'] == nome_pessoa:
        nova_idade = int(input('Digite a nova idade: '))
        try: 
            pessoa['idade'] = nova_idade
        except:
            print('O valor digitado não corresponde a um número.')        

print('')
for pessoa in pessoas:
    nome = pessoa['nome']
    idade = pessoa['idade']
    cidade = pessoa['cidade']
    print(f'• Nome: {nome} | Idade: {idade} | Cidade: {cidade}')

print('')
for pessoa in pessoas:
    nome = pessoa['nome']
    profissao = input(f'Qual é a profissão do(a) {nome}: ')
    pessoa['profissao'] = profissao

print('')
for pessoa in pessoas:
    nome = pessoa['nome']
    idade = pessoa['idade']
    cidade = pessoa['cidade']
    profissao_pessoa = pessoa['profissao']
    print(f'• Nome: {nome} | Idade: {idade} | Cidade: {cidade} | Profissão: {profissao_pessoa}')

nome_para_remover = input('\nQual o nome da pessoa que você deseja remover da lista? \n\nDigite aqui: ')

for pessoa in pessoas:
    if pessoa['nome'] == nome_para_remover:
        pessoas.remove(pessoa)

print('')
for pessoa in pessoas:
    nome = pessoa['nome']
    idade = pessoa['idade']
    cidade = pessoa['cidade']
    profissao_pessoa = pessoa['profissao']
    print(f'• Nome: {nome} | Idade: {idade} | Cidade: {cidade} | Profissão: {profissao_pessoa}')


#? EXERCICIO 03

print('')
quadrados_dos_numeros = [
    {
        'numero': 1,
        'quadrado': 1**2
    },
    {
        'numero': 2,
        'quadrado': 2**2
    },
    {
        'numero': 3,
        'quadrado': 3**2
    },
    {
        'numero': 4,
        'quadrado': 4**2
    },
    {
        'numero': 5,
        'quadrado': 5**2
    }
]

for numero in quadrados_dos_numeros:
    print(f'O quadrado do número: {numero['numero']} é {numero['quadrado']}')

#? EXERCICIO 04

dicionario = [
    {'nome': '','cidade': '','pais': '','genero': '','profissao': ''}
]

chave = 'bairro'

if chave in dicionario[0]:
    print(f'\nA chave "{chave}" existe no dicionário!')
else:
    print(f'\nA chave "{chave}" não existe no dicionário!')

#? EXERCICIO 05

print('')

livros = [
    {
        'titulo': 'O Código Perdido',
        'autor': 'Ana Souza',
        'ano': 2015,
        'história de vida do personagem': (
            "A história de vida do personagem é marcada por enigmas antigos. "
            "Sua história de vida também revela escolhas difíceis e mistérios escondidos."
        )
    },
    {
        'titulo': 'Segredos da Floresta',
        'autor': 'Carlos Lima',
        'ano': 2008,
        'história de vida do personagem': (
            "A história de vida do personagem é profundamente ligada à natureza. "
            "A cada página, sua conexão com a floresta mostra como a história de vida dele "
            "foi moldada pelo silêncio e pela força das árvores."
        )
    },
    {
        'titulo': 'O Último Guardião',
        'autor': 'Mariana Torres',
        'ano': 2020,
        'história de vida do personagem': (
            "A história de vida do personagem gira em torno da proteção de um legado antigo. "
            "Esse mesmo legado redefine sua própria história de vida, dando-lhe propósito e responsabilidade."
        )
    },
    {
        'titulo': 'Além do Horizonte',
        'autor': 'Pedro Almeida',
        'ano': 2012,
        'história de vida do personagem': (
            "A história de vida do personagem é feita de desafios e superações constantes. "
            "Sua história de vida se entrelaça com perdas dolorosas, mas também com vitórias que moldaram seu destino."
        )
    },
    {
        'titulo': 'Sombras do Passado',
        'autor': 'Juliana Mendes',
        'ano': 2018,
        'história de vida do personagem': (
            "A história de vida do personagem é marcada por segredos familiares. "
            "Esses segredos transformam a história de vida dele em um emaranhado de revelações e consequências inevitáveis."
        )
    }
]

for livro in livros:
    historia_personagem = livro['história de vida do personagem']
    contar_palavra = historia_personagem.count('de')
    print(contar_palavra)

print('')

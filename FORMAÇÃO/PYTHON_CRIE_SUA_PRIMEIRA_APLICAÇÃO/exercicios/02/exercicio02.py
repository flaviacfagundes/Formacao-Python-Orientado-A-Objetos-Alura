
#? EXERCICIO 01
print('')

num = int(input('Digite um número: '))

if num > 0:
    print('O número é positivo!')
elif num < 0:
    print('O número é negativo')
else: 
    print('O número é igual a 0')

#? EXERCICIO 02
print('')

idade = int(input('Digite a sua idade: '))

if 0 <= idade <= 12:
    print('Criança: 0 a 12 anos.')
elif 13 <= idade <= 18:
    print('Adolescente: 13 a 18 anos.')
elif idade > 18:
    print('Adulto: acima de 18 anos.')
else:
    print('Idade invalida')

#? EXERCICIO 03
print('')

user = 'Flávia'
password = '123456789'
usuario = input('Digite seu login: ')
senha = input('Digite sua senha: ')

if usuario == user and senha == password:
    print('Acesso concedido!')
else:
    print('Acesso negado!')

#? EXERCICIO 04
print('')

x = int(input('Digite a coordenada X: '))
y = int(input('Digite a coordenada Y: '))

if x > 0 and y > 0:
    print('Primeiro Quadrante')
elif x < 0 and y > 0:
    print('Segundo Quandrante')
elif x < 0 and y < 0:
    print('Terceiro Quadrante')
elif x > 0 and y < 0:
    print('Quarto Quadrante')
else:
    print('O Ponto Está No Centro')

print('')

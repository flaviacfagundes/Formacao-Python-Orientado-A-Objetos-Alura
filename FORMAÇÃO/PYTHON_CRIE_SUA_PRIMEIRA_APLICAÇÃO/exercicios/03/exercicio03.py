
#? EXERCICIO 01

print('')
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['Flavia', 'Cristina', 'Maria', 'Isabel']
ano = [2005, 2025]

#? EXERCICIO 02

cidades = ['Curitiba', 'São Paulo', 'Porto Alegre', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Manaus']

for cidade in cidades:
    print(f'• {cidade}')

print('')

#? EXERCICIO 03

somaNumerosImpares = 0

for i in range(0, 11):
    if (i %2 != 0):
        print(i)
        somaNumerosImpares += i

print('')
print(f'A soma dos números impares é igual a: {somaNumerosImpares}')
print('')

#? EXERCICIO 04

for d in range(10, -1, -1):
    print(d)

#? EXERCICIO 05

num = int(input('\nDigite um número e mostrarei a tabulada dele: '))
print('')

for n in range(0, 11):
    print(f'{num} x {n} = ', num * n)

#? EXERCICIO 06

print('')
listaDeNumeros = [1, 75, '32', 12, 56, 9, 45]
resultado = 0

for numero in listaDeNumeros:
    try:
        resultado += numero
        print(numero)
    except:
        print('O valor não corresponde a um número inteiro')

print(f'\nA soma dos números {listaDeNumeros} é igual a: {resultado}')

#? EXERCICIO 07

print('')
numerosParaMedia = [1, 2]
somaDosNumeros = 0

try:
    for numero in numerosParaMedia:
        somaDosNumeros += numero

    media = somaDosNumeros / len(numerosParaMedia)
    print(f'A média dos núemros {numerosParaMedia} é igual a {media}')

except:
    print('Lista vazia')

print('')

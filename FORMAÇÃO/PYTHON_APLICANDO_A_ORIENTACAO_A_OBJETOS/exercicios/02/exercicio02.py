
#? EXERCICIO 01 

print('')

class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurantes = []

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

#? EXERCICIO 02

print(restaurante_praca.categoria)
print('')

#? EXERCICIO 03

mensagem = 'Ativado' if restaurante_praca.ativo == True else 'Desativado'

print(mensagem)
print('')

#? EXERCICIO 04

categoria_restaurante = restaurante_praca.categoria

print(categoria_restaurante)
print('')

#? EXERCICIO 05

restaurante_praca.nome = 'Bistrô'

print(vars(restaurante_praca))
print('')

#? EXERCICIO 06

pizza_place = Restaurante()
pizza_place.nome = 'Pizza Place'
pizza_place.categoria = 'Fast Food'

#? EXERCICIO 07

print(vars(pizza_place))
print('')

#? EXERCICIO 08

pizza_place.ativo = True

print(pizza_place.ativo)

#? EXERCICIO 09

restaurantes.append(restaurante_praca)
restaurantes.append(pizza_place)

for restaurante in restaurantes:
    print('')
    print(f'Nome: {restaurante.nome} \nCategoria: {restaurante.categoria} \nStatus: {restaurante.ativo}')

print('')

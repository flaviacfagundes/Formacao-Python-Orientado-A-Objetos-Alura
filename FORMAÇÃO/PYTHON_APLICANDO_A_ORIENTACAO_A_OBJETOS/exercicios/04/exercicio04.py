
#? EXERCICIO 01

class Carro:
    carros = []

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)

    def mostrar_carros():
        for carro in Carro.carros:
            print('')
            print(f'• Modelo: {carro.modelo} \n• Cor: {carro.cor} \n• Ano: {carro.ano}')

        print('')

carro1 = Carro('Sandero', 'Vermelho', 2013)
carro2 = Carro('Ford Ka', 'Prata', 2009)
carro3 = Carro('Uno', 'Branco', 1998)

Carro.mostrar_carros()

#? EXERCICIO 02 

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, cidade, ano):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.cidade = cidade
        self.ano = ano
        Restaurante.restaurantes.append(self)

    def mostrar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print('')
            print(f'• Nome: {restaurante.nome} \n• Categoria: {restaurante.categoria} \n• Status Ativo: {restaurante.ativo} \n• Cidade: {restaurante.cidade} \n• Ano de Inauguração: {restaurante.ano}')
        
        print('')

restaurante1 = Restaurante('Bobs','Fast Food', 'Rio de Janeiro', 1951)
restaurante2 = Restaurante('KFC', 'Fast Food', 'Lake City', 1952)

Restaurante.mostrar_restaurantes()

#? EXERCICIO 03 | 04

class RestaurantePiloto:
    restaurantes = []

    def __init__(self, nome, categoria): 
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        RestaurantePiloto.restaurantes.append(self)

    def __str__(self):
        return f'- Nome: {self.nome} \n- Categoria: {self.categoria} \n- Status: {'Ativado' if self.ativo == True else 'Desativado'}'

piloto1 = RestaurantePiloto('Pizza', 'Italiana')
piloto2 = RestaurantePiloto('Sushi', 'Japonês')

print('')
print(piloto1)
print('')
print(piloto2)
print('')

#? EXERCICIO 05

class Cliente:
    clientes = []

    def __init__(self, nome, cpf, cidade):
        self.nome = nome
        self.cpf = cpf
        self.cidade = cidade
        self.logado = False
        Cliente.clientes.append(self)

    def mostrar_dados_clientes():
        for cliente in Cliente.clientes:
            print('')
            print(f'• Nome: {cliente.nome} \n• CPF: {cliente.cpf} \n• Cidade: {cliente.cidade} \n• Logado? {'Sim' if cliente.logado == True else 'Não'}')

        print('')

cliente1 = Cliente('Maria', 12345678910, 'Piracicaba')
cliente2 = Cliente('José', 10987654321, 'Taubaté')

Cliente.mostrar_dados_clientes()

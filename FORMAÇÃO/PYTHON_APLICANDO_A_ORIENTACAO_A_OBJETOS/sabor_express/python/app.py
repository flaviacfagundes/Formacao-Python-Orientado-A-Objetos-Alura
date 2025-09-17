
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): 
        self.nome = nome
        self.categoria = categoria
        self.status = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Nome: {self.nome} | Categoria: {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'Nome: {restaurante.nome} | Categoria: {restaurante.categoria} | Status: {restaurante.status}')

restaurante_burguer_king = Restaurante('Burger King', 'Fast Food')
restaurante_madero = Restaurante('Madero', 'Hamburgueria')

Restaurante.listar_restaurantes()

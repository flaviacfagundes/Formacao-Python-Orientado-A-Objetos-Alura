
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): 
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._status = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Nome: {self._nome} | Categoria: {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'\n-------------------------------'.ljust(31)} | {'------------------------------------'.ljust(36)} | {'-----------------------'}')
        print(f'{'NOME DO RESTAURANTE'.ljust(31)} | {'CATEGORIA'.ljust(36)} | {'STATUS'}')
        print(f'{'-------------------------------'.ljust(31)} | {'------------------------------------'.ljust(36)} | {'-----------------------'}')
        for restaurante in cls.restaurantes:
            print(f'Nome: {restaurante._nome.ljust(25)} | Categoria: {restaurante._categoria.ljust(25)} | Status: {restaurante.status}')
        
        print('')

    @property
    def status(self):
        return '✅ Ativado' if self._status else '❌ Desativado'
    
    def alterar_status(self):
        self._status = not self._status

restaurante_burguer_king = Restaurante('burger king', 'Fast Food')
restaurante_madero = Restaurante('madero', 'hamburgueria')
restaurante_burguer_king.alterar_status()

Restaurante.listar_restaurantes()

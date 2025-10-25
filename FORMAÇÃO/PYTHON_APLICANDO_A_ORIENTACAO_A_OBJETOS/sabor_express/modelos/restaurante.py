
from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): 
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._status = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Nome: {self._nome} | Categoria: {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'\n-------------------------------'.ljust(31)} | {'------------------------------------'.ljust(36)} | {'------------------------------------'.ljust(36)} | {'-----------------------'}')
        print(f'{'NOME DO RESTAURANTE'.ljust(31)} | {'CATEGORIA'.ljust(36)} | {'AVALIAÇÃO'.ljust(36)} | {'STATUS'}')
        print(f'{'-------------------------------'.ljust(31)} | {'------------------------------------'.ljust(36)} | {'------------------------------------'.ljust(36)} | {'-----------------------'}')
        for restaurante in cls.restaurantes:
            print(f'Nome: {restaurante._nome.ljust(25)} | Categoria: {restaurante._categoria.ljust(25)} | Avaliação: {str(restaurante.media_avaliacoes).ljust(25)} | Status: {restaurante.status}')
        
        print('')

    @property
    def status(self):
        return '✅ Ativado' if self._status else '❌ Desativado'
    
    def alterar_status(self):
        self._status = not self._status

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas / quantidade_notas, 1)
        return media


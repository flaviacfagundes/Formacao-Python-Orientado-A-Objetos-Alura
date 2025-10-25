
from modelos.avaliacao import Avaliacao

class Restaurante:
    """Representa um restaurante e suas características."""

    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (`str`): O nome do restaurante.
        - categoria (`str`): A categoria do restaurante.
        """
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._status = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f'Nome: {self._nome} | Categoria: {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f'{'\n-------------------------------'.ljust(31)} | {'------------------------------------'.ljust(36)} | {'------------------------------------'.ljust(36)} | {'-----------------------'}')
        print(f'{'NOME DO RESTAURANTE'.ljust(31)} | {'CATEGORIA'.ljust(36)} | {'AVALIAÇÃO'.ljust(36)} | {'STATUS'}')
        print(f'{'-------------------------------'.ljust(31)} | {'------------------------------------'.ljust(36)} | {'------------------------------------'.ljust(36)} | {'-----------------------'}')
        for restaurante in cls.restaurantes:
            print(f'Nome: {restaurante._nome.ljust(25)} | Categoria: {restaurante._categoria.ljust(25)} | Avaliação: {str(restaurante.media_avaliacoes).ljust(25)} | Status: {restaurante.status}')
        
        print('')

    @property
    def status(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '✅ Ativado' if self._status else '❌ Desativado'
    
    def alterar_status(self):
        """Alterna o estado de atividade do restaurante."""
        self._status = not self._status

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (`str`): O nome do cliente que fez a avaliação.
        - nota (`float`): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if nota > 5:
            nota = 5
        elif nota < 0:
            nota = 0
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao:
            return 'Sem avaliação'
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas / quantidade_notas, 1)
        return media


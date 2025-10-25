
#? EXERCICIO 01 | 02 | 03 | 04

class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = int(ano_publicacao)
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'\n• Titulo: {self._titulo} \n• Autor: {self._autor} \n• Ano de Publicação: {self._ano_publicacao}\n• Disponibilidade: {self.disponivel}\n'
    
    @property
    def disponivel(self):
        return f'Disponível' if self._disponivel == True else 'Indisponível'
    
    def emprestar(self):
        self._disponivel = not self._disponivel

    def verificar_disponibilidade(ano):
        for livro in Livro.livros:
            if livro._ano_publicacao == ano:
                print(f'\n======== Livros de {ano} ========')
                print(livro)


livro1 = Livro('Entendendo Algoritmos', 'Aditya Y. Bhargava', 2017)
livro2 = Livro('Código Limpo', 'Robert Cecil Martin', 2008)

print(livro1)
print(livro2)

livro1.emprestar()

print('--------------------------------')
print(livro1)
print(livro2)

print('--------------------------------')
Livro.verificar_disponibilidade(2008)

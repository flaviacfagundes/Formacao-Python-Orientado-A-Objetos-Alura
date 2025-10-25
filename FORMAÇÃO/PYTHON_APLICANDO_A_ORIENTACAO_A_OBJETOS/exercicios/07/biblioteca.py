from exercicio07 import Livro

#? EXERCICIOS 05 | 06 | 07 

livro3 = Livro('Padrões de Projeto', 'Erich Gamma', 1994)
livro4 = Livro('Arquitetura Limpa', 'Robert Cecil Martin', 2017)
livro5 = Livro('Use a Cabeça! Python', 'Paul Barry', 2016)

livro4.emprestar()

print('--------------------------------')
print(livro3)
print(livro4)
print(livro5)

print('--------------------------------')
Livro.verificar_disponibilidade(1994)

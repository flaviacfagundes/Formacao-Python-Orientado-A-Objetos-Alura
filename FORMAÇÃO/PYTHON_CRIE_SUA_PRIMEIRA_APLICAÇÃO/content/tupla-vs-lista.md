
# Tuplas vs Listas

As **tuplas** são estruturas de dados que nos permitem armazenar elementos de maneira ordenada e sequencial, assim como as **listas**. Dessa forma, ambas mantêm a ordem dos elementos e oferecem índices para acessar esses valores.

Contudo, existem diferenças fundamentais entre tuplas e listas que as tornam adequadas para diferentes situações.

## Sixtaxe

O primeiro ponto que diferencia esses dois arranjos é a sintaxe de cada um. As **listas** são definidas utilizando colchetes `[ ]`, enquanto as **tuplas** são definidas utilizando parênteses `( )`.

~~~~
lista = [1,’olá mundo’,True,9.7]
tupla = (1,’olá mundo’,True,9.7)
~~~~

## Mutabilidade

A maior diferença entre essas duas configurações são suas propriedades de mutabilidade.

As **listas são estruturas mutáveis**, o que significa que é possível modificar seus elementos, adicionar novos itens ou remover existentes após a criação da lista, podendo inclusive utilizar funções próprias para isso como `append()`, `remove()`, `pop()`, e `insert()`.

Ao contrário das listas, **tuplas são imutáveis**. Uma vez que uma tupla é criada, seus elementos não podem ser alterados, adicionados ou removidos.

## Desempenho

Devido à sua imutabilidade, as **tuplas** têm um desempenho melhor do que **listas** para algumas operações. Elas são mais eficientes em termos de espaço e processamento em determinados cenários.

Sendo assim, **listas** podem ser menos eficientes em termos de desempenho para operações específicas, especialmente quando se trata de manipulação de grandes conjuntos de dados, devido à sua mutabilidade.

## Quando devo utilizar cada estrutura

- As **listas** são ideais quando você precisa de uma coleção de elementos que pode ser modificada ao longo do tempo. 
- As **tuplas** são apropriadas quando se deseja garantir que os elementos não sejam alterados após a criação. Isso é útil para dados que devem permanecer constantes ao longo do tempo.

---

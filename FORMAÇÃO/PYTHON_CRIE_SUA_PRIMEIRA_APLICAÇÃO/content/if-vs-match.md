
# Qual Instrução Usar?

O `if` nos proporciona uma maneira eficaz de tomar decisões simples ou complexas em nosso código, adaptando o comportamento do programa de acordo com as circunstâncias determinadas. Ao usar `match`, podemos simplificar a lógica do código em situações que envolvem múltiplos padrões complexos. Ela oferece uma estrutura mais legível, especialmente quando temos diversos casos a serem tratados.

| Vantagens da Instrução `match` | Vantagens da Estrutura `if`| 
|:---------------------------------------|:---------------------------------------|
| Lidar com condições complexas e múltiplos padrões de maneira mais intuitiva. | Implementação clássica e amplamente conhecida. |
| Sintaxe concisa melhora a legibilidade do código, especialmente em casos complexos. | Amplamente suportada em todas as versões do Python. |
| Permite desestruturação direta, evitando repetição excessiva de variáveis. | Estrutura simples e direta para lógica condicional básica. |
| Adiciona expressividade ao código, especialmente em situações de correspondência de padrões. | Pode ser mais intuitiva para devs familiarizados com estruturas de controle convencionais. |

## Sintaxe If, Elif e Else

~~~
opcao_escolhida = int(input('Escolha uma opção: '))
if opcao_escolhida == 1:
    print('Adicionar restaurante')
elif opcao_escolhida == 2:
    print('Listar restaurantes')
elif opcao_escolhida == 3:
    print('Ativar restaurante')
elif opcao_escolhida == 4:
    print('Finalizar app')
else:
    print('Opção inválida!')
~~~

## Sixtaxe Match

~~~
match expressão:
    case padrão_1:
        # Código a ser executado se expressão corresponder a padrão_1
    case padrão_2:
        # Código a ser executado se expressão corresponder a padrão_2
    # ... outros casos ...
    case _:
        # Código a ser executado se nenhum dos padrões anteriores corresponder. Isso é útil para tratar casos não específicos.
~~~

---

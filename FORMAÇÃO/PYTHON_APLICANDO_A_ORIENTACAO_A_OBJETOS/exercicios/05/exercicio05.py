
class Pessoa:
    def __init__(self, nome, idade, profissao, cidade):
        self._nome = nome
        self._idade = int(idade)
        self._profissao = profissao
        self._cidade = cidade
    
    def __str__(self):
        return f'\n→ Nome: {self._nome} \n→ Idade: {self._idade} \n→ Profissão: {self._profissao} \n→ Cidade: {self._cidade}\n'
    
    def aniversario(self):
        self._idade += 1

    def saudacao(self):
        print(f'Olá, {self._profissao}! Que sua jornada seja produtiva hoje.')


pessoa1 = Pessoa('Flávia', '20', 'Assistente', 'Curitba')
print(pessoa1)

pessoa1.aniversario()
pessoa1.saudacao()

print(pessoa1)

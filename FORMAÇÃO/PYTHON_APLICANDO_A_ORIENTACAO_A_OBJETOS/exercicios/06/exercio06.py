
#? EXERCICIO 01 | 02 | 03

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = float(saldo)
        self._ativo = False

    def __str__(self):
        return f'\nTitular: {self.titular} | Saldo: {self.saldo}'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

conta1 = ContaBancaria('Maria', 1000)
conta2 = ContaBancaria('João', 2000)

print(conta1)
print(conta2)

print(f'\nAntes de Ativar | Conta Ativa? {conta1._ativo}')
ContaBancaria.ativar_conta(conta1)
print(f'Depois de Ativar | Conta Ativa? {conta1._ativo}\n')

#? EXERCICIO 04 | 05

class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = float(saldo)
        self._ativo = False

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo
    
conta3 = ContaBancariaPythonica('Laura', '5000')
print(f'Titular da Conta 3: {conta3.titular}\n')

#? EXERCIO 06 | 07

class ClienteBanco:
    def __init__(self, nome, email, cidade, saldo):
        self._nome = nome
        self._email = email
        self._cidade = cidade
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'\nNome: {self._nome} \nEmail: {self._email} \nCidade: {self._cidade} \nSaldo: {self._saldo} \nStatus: {self.ativo}\n'
    
    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Desativado'
    
    @classmethod
    def depositar(cls, cliente, valor):
        cliente._saldo = cliente._saldo + valor

    @classmethod
    def sacar(cls, cliente, valor):
        cliente._saldo = cliente._saldo - valor

cliente1 = ClienteBanco('Gabriel', 'gabriel@gmail.com', 'Piracicaba', 30000)
print(cliente1)
cliente1.depositar(cliente1, 10000)
print(cliente1)
cliente1.sacar(cliente1, 35000)
print(cliente1)

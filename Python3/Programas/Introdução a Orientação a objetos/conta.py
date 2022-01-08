
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("criando objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite =limite

    def extrato(self):
        print("O saldo do titular {}, é de {}.".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_sacar = self.saldo + self.limite
        return  valor_a_sacar <= valor_disponivel_sacar


    def saca(self, valor):
        if(self.__pode_sacar(valor))
            self.__saldo -= valor
        else:
            print("Você não tem saldo suficiente")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"
    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}


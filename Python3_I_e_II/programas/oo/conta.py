
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("criando objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite =limite

    def extrato(self):
        print("O saldo do titular {}, é de {}.".format(self.titular, self.saldo))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor




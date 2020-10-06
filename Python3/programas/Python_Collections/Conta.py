from functools import total_ordering

@total_ordering
class Conta:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __add__(self, other):
        if isinstance(other, int):
            self.deposita(other)

    def __eq__(self, other):
        if type(other) != Conta:
            return False

        return self._codigo == other._codigo and self._saldo == other._saldo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        return self._codigo < other._codigo

    def deposita(self, valor):
        self._saldo += valor

    def saldo(self):
        return self._saldo

    def __str__(self):
        return "[>> Codigo {} Saldo {} <<]".format(self._codigo,self._saldo)



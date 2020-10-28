from validate_docbr import CPF
from validate_docbr import CNPJ


class Cpf:

    def __init__(self, documento, tipo):
        self.tipo = tipo
        documento = str(documento)
        if tipo == "cpf":
            if self.valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido")
        elif tipo == "cnjp":


    def validoCpf(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Número de digitos inválido")

    def formatacao(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.formatacao()

    def validoCnpj(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)
        else:
            raise ValueError("Número de digitos inválido")

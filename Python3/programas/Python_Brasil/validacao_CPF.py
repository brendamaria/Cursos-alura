from validate_docbr import CPF

class Cpf:

    def __init__(self, documento):
        documento = str(documento)
        if self.valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido")

    def valido(self, cpf):
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
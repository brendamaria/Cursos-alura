from validate_docbr import CNPJ


class Cnpj:

    def __init__(self, documento):
        documento = str(documento)
        if self.valido(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido")

    def valido(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)
        else:
            raise ValueError("Número de digitos inválido")

    def formatacao(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        return self.formatacao()

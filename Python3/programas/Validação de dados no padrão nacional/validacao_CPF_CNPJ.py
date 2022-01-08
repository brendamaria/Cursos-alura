from validate_docbr import CPF, CNPJ


class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return Cpf(documento)
        elif len(documento) == 14:
            return Cnpj(documento)
        else:
            raise ValueError("Número de digitos inválido")


class Cpf:

    def __init__(self, documento):
        if self.validador(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return self.format()

    def validador(self, documento):
        valida = CPF()
        return valida.validate(documento)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class Cnpj:

    def __init__(self, documento):
        if self.validador(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido")

    def __str__(self):
        return self.format()

    def validador(self, documento):
        valida = CNPJ()
        return valida.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

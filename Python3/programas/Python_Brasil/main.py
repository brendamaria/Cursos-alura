from validacao_telefone import TelefonesBr
from validacao_CPF_CNPJ import Documento

print("------ VALIDAÇÃO DE TELEFONE ------")
telefone = "552126481234"
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)


print("------ VALIDAÇÃO DE CPF ------")
exemplo_cpf = "32007832062"
documento_cpf = Documento.cria_documento(exemplo_cpf)
print(documento_cpf)


print("------ VALIDAÇÃO DE CNPJ ------")
exemplo_cnpj = "35379838000112"
documento_cnpj = Documento.cria_documento(exemplo_cnpj)
print(documento_cnpj)
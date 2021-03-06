from validacao_telefone import TelefonesBr
from validacao_CPF_CNPJ import Documento
from datas import Datas
from valida_CEP import BuscaEndereco
import requests

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

print("------ DATAS ------")
cadastro = Datas()
print("-- Momento do Cadastro --")
print(cadastro.momento_cadastro)
print("-- Mes do Cadastro --")
print(cadastro.mes_cadastro())
print("-- Dia do Cadastro --")
print(cadastro.dia_semana())
print("-- Formatação --")
print(cadastro.data_formatada())
print("-- Tempo Cadastro --")
print(cadastro.tempo_cadastro())

print("-- Endereços --")
cep = "70673410"
cep_obj = BuscaEndereco(cep)
print(cep_obj)


bairro, localidade, uf = BuscaEndereco.retorna_endereco(cep_obj)
print(bairro, localidade, uf)

